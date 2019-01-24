## Depend: Python 3.7.2
# pip install pyserial pyinstaller PyQt5
#
## Create exe:
# pyinstaller --log-level=WARN --add-binary="esptool.exe;." --add-binary="esptool.py;." --add-binary="espLogo.png;." --noconfirm --noconsole --onefile ESPFlasherGUI.py # --clean --upx-dir=C:/Setup/upx
#

import sys, os, io
import serial.tools.list_ports
import os.path

from PyQt5 import QtCore , QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QShortcut
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QKeySequence

import esptoolGUIUI
		
class ESPToolGUIApp(QtWidgets.QMainWindow,esptoolGUIUI.Ui_MainWindow):
    def __init__(self,parent=None):
        super(ESPToolGUIApp,self).__init__(parent)
        if getattr(sys, 'frozen', False):
            self.frozen = 'ever so'
            self.bundle_dir = sys._MEIPASS
        else:
            self.bundle_dir = os.path.dirname(os.path.abspath(__file__))
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(self.bundle_dir+'/espLogo.png'))
        self.memoryESP8266 = ['detect','512KB','256KB','1MB','2MB','4MB','2MB-c1','4MB-c1','4MB-c2']
        self.memoryESP32 = ['detect','1MB','2MB','4MB','8MB','16MB']
        self.cmdList = ['TEXT1','TEXT2']
        self.ser = serial.Serial()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.tick)
        self.timer.start(50) 
		
        self.initButtons()
        self.initProcess()
        self.baudRate = 921600
        self.port = ''
        self.flasSize = self.comboBoxMemory.currentText()
        self.frozen = 'not'
        self.chip = 'ESP32'
		
    def resizeEvent(self,ev):
        w = int(str(self.geometry()).split("(")[1].split(")")[0].split(",")[2])
        h = int(str(self.geometry()).split("(")[1].split(")")[0].split(",")[3])
        #print (w,h)
        self.verticalLayoutWidget.resize(w,h)

    def selectFile(self,name,obj):
        files, _ = QFileDialog.getOpenFileName(self,name,filter='(*.bin)')
        obj.setText(files)

    def baudSelect(self):
        self.baudRate = int(self.comboBoxBaudSelect.currentText())

    def portSelect(self):
        self.port = self.lineEditCOMPort.text()

    def flashSizeSelect(self):
        self.flasSize = self.comboBoxMemory.currentText()

    def dataReady(self):
        #self.plainTextEditStatus.appendPlainText(str(self.process.readAllStandardOutput()))
        self.plainTextEditStatus.appendPlainText(bytearray(self.process.readAllStandardOutput()).decode('utf-8'))		

    def initProcess(self):
        self.process = QtCore.QProcess(self)

        self.process.setProcessChannelMode(QtCore.QProcess.MergedChannels)
        self.process.readyRead.connect(self.dataReady)
        self.process.started.connect(self.disableButtons)
        self.process.finished.connect(self.enableButtons)

    def disableButtons(self):
        self.pushButtonErase.setDisabled(True)
        self.pushButtonFlashAll.setDisabled(True)
        self.pushButtonFlashBoot.setDisabled(True)		
        self.pushButtonFlash.setDisabled(True)		
        self.pushButtonPartition.setDisabled(True)
        self.pushButtonBootloader.setDisabled(True)
        self.pushButtonApplication.setDisabled(True)
        self.comboBoxMemory.setDisabled(True)
        self.comboBoxCOMPort.setDisabled(True)
        self.comboBoxBaudSelect.setDisabled(True)
        self.pushButtonSend.setDisabled(True)
        self.pushButtonOpen.setDisabled(True)
        self.pushButtonClose.setDisabled(True)		
		
    def enableButtons(self):
        if (self.chip=='ESP32'):
            self.pushButtonErase.setDisabled(False)
            self.pushButtonFlashAll.setDisabled(False)
            self.pushButtonFlash.setDisabled(False)
            self.pushButtonFlashBoot.setDisabled(False)			
            self.pushButtonPartition.setDisabled(False)
            self.pushButtonBootloader.setDisabled(False)
            self.pushButtonApplication.setDisabled(False)
            self.comboBoxMemory.setDisabled(False)
            self.comboBoxCOMPort.setDisabled(False)
            self.comboBoxBaudSelect.setDisabled(False)
            self.pushButtonSend.setDisabled(False)
            self.pushButtonOpen.setDisabled(False)
            self.pushButtonClose.setDisabled(False)			
        else:
            self.pushButtonErase.setDisabled(False)
            self.pushButtonFlash.setDisabled(False)
            self.pushButtonBootloader.setDisabled(False)
            self.comboBoxMemory.setDisabled(False)
            self.comboBoxCOMPort.setDisabled(False)
            self.comboBoxBaudSelect.setDisabled(False)

    def initButtons(self):
        self.pushButtonBootloader.clicked.connect(lambda: self.selectFile('Select Bootloader File',self.labelBootloader))
        self.pushButtonPartition.clicked.connect(lambda: self.selectFile('Select Partition File',self.labelPartition))
        self.pushButtonApplication.clicked.connect(lambda: self.selectFile('Select Application File',self.labelApplication))
        self.pushButtonApplication.setToolTip('F8 - Select firmware')

        self.pushButtonErase.clicked.connect(self.erase)
        self.pushButtonFlash.clicked.connect(self.flash)
        self.pushButtonFlash.setToolTip('F12 - Flash firmware')
        self.pushButtonFlashAll.clicked.connect(self.flash_all)
        self.pushButtonFlashAll.setToolTip('F5 - Flash boot loader+partition+firmware')
        self.pushButtonFlashBoot.clicked.connect(self.flash_boot)		
        self.pushButtonFlashBoot.setToolTip('F9 - Flash boot loader+partition')
		
        self.pushButtonSend.clicked.connect(self.send_cmd)
        self.pushButtonSend.setToolTip('F4 - Send data')		
        self.pushButtonOpen.clicked.connect(self.open_serial)
        self.pushButtonOpen.setToolTip('F3 - Open serial port')				
        self.pushButtonClose.clicked.connect(self.close_serial)
        self.pushButtonClose.setToolTip('Ctrl+F4 - Close serial port')						
        self.pushButtonClear.clicked.connect(self.clear_log)
        self.pushButtonClear.setToolTip('F7 - Clear log')						
		
        self.comboBoxBaudSelect.addItems(['921600','512000','256000','230400','115200'])
        self.comboBoxBaudSelect.currentIndexChanged.connect(self.baudSelect)
        self.baudRate = int(self.comboBoxBaudSelect.currentText())
		
        self.comboBoxChipSelect.addItems(['ESP32','ESP8266'])
        self.comboBoxChipSelect.currentIndexChanged.connect(self.chipSelect)
        comPort = []
        try:
            for x in serial.tools.list_ports.comports():
                comPort.append(str(x.device))
        except IndexError:
                pass
        self.comboBoxCOMPort.addItems(comPort)
        self.comboBoxCOMPort.popupAboutToBeShown.connect(self.comPortClick)
        self.comboBoxCOMPort.currentIndexChanged.connect(self.comPortSelect)
        self.port = self.comboBoxCOMPort.currentText()
		
        self.comboBoxCmd.addItems(self.cmdList)
        self.comboBoxMemory.addItems(self.memoryESP32)
        self.comboBoxMemory.currentIndexChanged.connect(self.memorySelect)
        self.flasSize = self.comboBoxMemory.currentText()

        self.flashAllShortcut = QShortcut(QKeySequence("F5"), self)
        self.flashAllShortcut.activated.connect(self.flash_all)
        self.flashBootShortcut = QShortcut(QKeySequence("F9"), self)
        self.flashBootShortcut.activated.connect(self.flash_boot)
        self.flashShortcut = QShortcut(QKeySequence("F12"), self)
        self.flashShortcut.activated.connect(self.flash)
        self.OpenShortcut = QShortcut(QKeySequence("F3"), self)
        self.OpenShortcut.activated.connect(self.open_serial)
        self.CloseShortcut = QShortcut(QKeySequence("Ctrl+F4"), self)
        self.CloseShortcut.activated.connect(self.close_serial)
        self.SendShortcut = QShortcut(QKeySequence("F4"), self)
        self.SendShortcut.activated.connect(self.send_cmd)
        self.ClearShortcut = QShortcut(QKeySequence("F7"), self)
        self.ClearShortcut.activated.connect(self.clear_log)
        self.SelectShortcut = QShortcut(QKeySequence("F8"), self)
        self.SelectShortcut.activated.connect(lambda: self.selectFile('Select Application File',self.labelApplication))
		
    def memorySelect(self):
        self.flasSize = self.comboBoxMemory.currentText()

    def comPortClick(self):
        comPort = []
        try:
            for x in serial.tools.list_ports.comports():
                comPort.append(str(x.device))
        except IndexError:
                pass
        self.comboBoxCOMPort.clear()
        self.comboBoxCOMPort.addItems(comPort)
		
    def comPortSelect(self):
        self.port = self.comboBoxCOMPort.currentText()

    def chipSelect(self):
        self.chip = self.comboBoxChipSelect.currentText()
        if (self.chip=='ESP8266'):
            self.pushButtonBootloader.setText('Firmware')
            self.labelBootloader.setText('Firmware')
            self.pushButtonPartition.setDisabled(True)
            self.pushButtonApplication.setDisabled(True)
            self.comboBoxMemory.clear()
            self.comboBoxMemory.addItems(self.memoryESP8266)
        else:
            self.pushButtonBootloader.setText('Bootlader')
            self.labelBootloader.setText('bootloader.bin')
            self.pushButtonPartition.setEnabled(True)
            self.pushButtonApplication.setEnabled(True)
            self.comboBoxMemory.clear()
            self.comboBoxMemory.addItems(self.memoryESP32)


    def erase(self):
        self.plainTextEditStatus.appendPlainText("Not support.")
        return
        self.port = self.comboBoxCOMPort.currentText()
        if (os.name=='nt'):
            if (self.chip=='ESP32'):
                self.process.start(self.bundle_dir+'/esptool.exe --chip esp32 --port {0} --baud {1} erase_flash'.format(self.port,self.baudRate))
            if (self.chip=='ESP8266'):
                self.process.start(self.bundle_dir+'/esptool.exe --chip esp8266 --port {0} --baud {1} erase_flash'.format(self.port,self.baudRate))
        else:
            if (self.chip=='ESP32'):
                self.process.start('sudo python '+self.bundle_dir+'/esptool.py --chip esp32 --port {0} --baud {1} erase_flash'.format(self.port,self.baudRate))
            else:
                self.process.start('sudo python '+self.bundle_dir+'/esptool.py --chip esp8266 --port {0} --baud {1} erase_flash'.format(self.port,self.baudRate))

    def flash(self):
        self.port = self.comboBoxCOMPort.currentText()
        if (self.labelApplication.text() == ""):
            self.plainTextEditStatus.appendPlainText("Error: Firmware is missing.")
            return
        self.ser.close()
        if (os.name=='nt'):
            if (self.chip=='ESP32'):
                cmd = (self.bundle_dir+'/esptool.exe --chip esp32 --port {0} --baud {1}\
                                    --before default_reset --after hard_reset write_flash\
                                    -z --flash_freq 80m --flash_mod dio --flash_size {2} \
                                    0x10000 {3}'.format(self.port,self.baudRate,self.flasSize,self.labelApplication.text()))
                self.process.start(self.bundle_dir+'/esptool.exe --chip esp32 --port {0} --baud {1}\
                                    --before default_reset --after hard_reset write_flash\
                                    -z --flash_freq 80m --flash_mod dio --flash_size {2} \
                                    0x10000 {3}'.format(self.port,self.baudRate,self.flasSize,self.labelApplication.text()))
            else:
                self.process.start(self.bundle_dir+'/esptool.exe --chip esp8266 --port {0} --baud {1}\
                                    --before default_reset --after hard_reset write_flash --flash_size={2}\
                                     0 {3}'.format(self.port,self.baudRate,self.flasSize,self.labelBootloader.text()))
        else:
            if (self.chip=='ESP32'):
                self.process.start('sudo python '+self.bundle_dir+'/esptool.py --chip esp32 --port {0} --baud {1}\
                                --before default_reset --after hard_reset write_flash\
                                -z --flash_freq 80m --flash_mod dio --flash_size {2} \
                                0x10000 {3}'.format(self.port,self.baudRate,self.flasSize,self.labelApplication.text()))
            else:
                self.process.start('sudo python '+self.bundle_dir+'/esptool.py --chip esp8266 --port {0} --baud {1}\
                                --before default_reset --after hard_reset write_flash --flash_size={2}\
                                 0 {3}'.format(self.port,self.baudRate,self.flasSize,self.labelBootloader.text()))
    def flash_boot(self):
        if not os.path.isfile(self.labelBootloader.text()):
            self.plainTextEditStatus.appendPlainText("Error: invalid bootloader file.")
            return
        if not os.path.isfile(self.labelPartition.text()):
            self.plainTextEditStatus.appendPlainText("Error: invalid partition file.")
            return
        self.port = self.comboBoxCOMPort.currentText()
        self.ser.close()
        if (os.name=='nt'):
            if (self.chip=='ESP32'):
                cmd = (self.bundle_dir+'/esptool.exe --chip esp32 --port {0} --baud {1}\
                                    --before default_reset --after hard_reset write_flash\
                                    -z --flash_freq 80m --flash_mod dio --flash_size {2} \
                                    0x1000 {3} 0x8000 {4}'.format(self.port,self.baudRate,self.flasSize,self.labelBootloader.text(),self.labelPartition.text()))

                self.process.start(self.bundle_dir+'/esptool.exe --chip esp32 --port {0} --baud {1}\
                                    --before default_reset --after hard_reset write_flash\
                                    -z --flash_freq 80m --flash_mod dio --flash_size {2} \
                                    0x1000 {3} 0x8000 {4}'.format(self.port,self.baudRate,self.flasSize,self.labelBootloader.text(),self.labelPartition.text()))
            else:
                self.process.start(self.bundle_dir+'/esptool.exe --chip esp8266 --port {0} --baud {1}\
                                    --before default_reset --after hard_reset write_flash --flash_size={2}\
                                     0 {3}'.format(self.port,self.baudRate,self.flasSize,self.labelBootloader.text()))
        else:
            if (self.chip=='ESP32'):
                self.process.start('sudo python '+self.bundle_dir+'/esptool.py --chip esp32 --port {0} --baud {1}\
                                --before default_reset --after hard_reset write_flash\
                                -z --flash_freq 80m --flash_mod dio --flash_size {2} \
                                0x1000 {3} 0x8000 {4}'.format(self.port,self.baudRate,self.flasSize,self.labelBootloader.text(),self.labelPartition.text()))
            else:
                self.process.start('sudo python '+self.bundle_dir+'/esptool.py --chip esp8266 --port {0} --baud {1}\
                                --before default_reset --after hard_reset write_flash --flash_size={2}\
                                 0 {3}'.format(self.port,self.baudRate,self.flasSize,self.labelBootloader.text()))

    def flash_all(self):
        if not os.path.isfile(self.labelBootloader.text()):
            self.plainTextEditStatus.appendPlainText("Error: invalid bootloader file.")
            return
        if not os.path.isfile(self.labelPartition.text()):
            self.plainTextEditStatus.appendPlainText("Error: invalid partition file.")
            return
#        if not os.path.isfile(self.labelApplication.text()):
#            self.plainTextEditStatus.appendPlainText("Error: invalid firmware file.")
#            return			
        self.port = self.comboBoxCOMPort.currentText()
        self.ser.close()
        if (os.name=='nt'):
            if (self.chip=='ESP32'):
                self.process.start(self.bundle_dir+'/esptool.exe --chip esp32 --port {0} --baud {1}\
                                    --before default_reset --after hard_reset write_flash\
                                    -z --flash_freq 80m --flash_mod dio --flash_size {2} \
                                    0x1000 {3} 0x8000 {4} 0x10000 {5}'.format(self.port,self.baudRate,self.flasSize,self.labelBootloader.text(),self.labelPartition.text(),self.labelApplication.text()))
            else:
                self.process.start(self.bundle_dir+'/esptool.exe --chip esp8266 --port {0} --baud {1}\
                                    --before default_reset --after hard_reset write_flash --flash_size={2}\
                                     0 {3}'.format(self.port,self.baudRate,self.flasSize,self.labelBootloader.text()))
        else:
            if (self.chip=='ESP32'):
                self.process.start('sudo python '+self.bundle_dir+'/esptool.py --chip esp32 --port {0} --baud {1}\
                                --before default_reset --after hard_reset write_flash\
                                -z --flash_freq 80m --flash_mod dio --flash_size {2} \
                                0x1000 {3} 0x8000 {4} 0x10000 {5}'.format(self.port,self.baudRate,self.flasSize,self.labelBootloader.text(),self.labelPartition.text(),self.labelApplication.text()))
            else:
                self.process.start('sudo python '+self.bundle_dir+'/esptool.py --chip esp8266 --port {0} --baud {1}\
                                --before default_reset --after hard_reset write_flash --flash_size={2}\
                                 0 {3}'.format(self.port,self.baudRate,self.flasSize,self.labelBootloader.text()))
								 
    def open_serial(self):
        self.port = self.comboBoxCOMPort.currentText()
        try:
            if self.ser.is_open==False:
                self.ser = serial.Serial(self.port, baudrate=115200, timeout=0, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, rtscts=False, dsrdtr=False)                
            if self.ser.is_open==True:
                self.plainTextEditStatus.appendPlainText("Success!")
        except:
            self.plainTextEditStatus.appendPlainText("Error!")
			
    def close_serial(self):
        self.port = self.comboBoxCOMPort.currentText()
        self.ser.close()
        self.plainTextEditStatus.appendPlainText("Closed!")
		
    def send_cmd(self):
        self.port = self.comboBoxCOMPort.currentText()
        try:
            if self.ser.is_open==False:
                self.ser = serial.Serial(self.port, baudrate=115200, timeout=0, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, rtscts=False, dsrdtr=False)
            if self.ser.is_open==True:
                self.ser.write(self.comboBoxCmd.currentText().encode())            
        except:
            print("Error")
            pass

    def tick(self):
        if self.ser.is_open == True:
            try:
                s = self.ser.read(512)
                if len(s) > 0:
                    self.plainTextEditStatus.appendPlainText(s.decode('utf-8'))
                    #print(s.decode('utf-8'))
            except:
                pass
    def clear_log(self):
        self.port = self.comboBoxCOMPort.currentText()
        self.plainTextEditStatus.clear()
		
def main():
    app = QtWidgets.QApplication(sys.argv)
    windows = ESPToolGUIApp()
    windows.show()
    app.exec_()

if __name__=='__main__':
    main()
