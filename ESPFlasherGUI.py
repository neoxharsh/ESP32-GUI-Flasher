import sys, os
import esptoolGUIUI
from PyQt4 import QtGui, QtCore

class ESPToolGUIApp(QtGui.QMainWindow,esptoolGUIUI.Ui_MainWindow):
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
        self.initButtons()
        self.initProcess()
        self.baudRate = 921600
        self.port = 'COM16'
        self.flasSize = '4M'
        self.frozen = 'not'
        self.chip = 'ESP32'

    def selectFile(self,name,obj):
        obj.setText(QtGui.QFileDialog.getOpenFileName(self,name,filter='(*.bin)'))

    def baudSelect(self):
        self.baudRate = int(self.comboBoxBaudSelect.currentText())

    def portSelect(self):
        self.port = self.lineEditCOMPort.text()

    def flashSizeSelect(self):
        self.flasSize = self.lineEditMemory.text()

    def dataReady(self):
        self.plainTextEditStatus.appendPlainText(str(self.process.readAllStandardOutput()))

    def initProcess(self):
        self.process = QtCore.QProcess(self)

        self.process.setProcessChannelMode(QtCore.QProcess.MergedChannels)
        self.process.readyRead.connect(self.dataReady)
        self.process.started.connect(self.disableButtons)
        self.process.finished.connect(self.enableButtons)

    def disableButtons(self):
        self.pushButtonErase.setDisabled(True)
        self.pushButtonFlash.setDisabled(True)
        self.pushButtonPartition.setDisabled(True)
        self.pushButtonBootloader.setDisabled(True)
        self.pushButtonApplication.setDisabled(True)
        self.comboBoxMemory.setDisabled(True)
        self.comboBoxCOMPort.setDisabled(True)
        self.comboBoxBaudSelect.setDisabled(True)

    def enableButtons(self):
        if (self.chip=='ESP32'):
            self.pushButtonErase.setDisabled(False)
            self.pushButtonFlash.setDisabled(False)
            self.pushButtonPartition.setDisabled(False)
            self.pushButtonBootloader.setDisabled(False)
            self.pushButtonApplication.setDisabled(False)
            self.comboBoxMemory.setDisabled(False)
            self.comboBoxCOMPort.setDisabled(False)
            self.comboBoxBaudSelect.setDisabled(False)
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
        self.pushButtonFlash.clicked.connect(self.flash)
        self.pushButtonErase.clicked.connect(self.erase)

        self.comboBoxBaudSelect.addItems(['921600','512000','256000','230400','115200'])
        self.comboBoxBaudSelect.currentIndexChanged.connect(self.baudSelect)

        self.comboBoxChipSelect.addItems(['ESP32','ESP8266'])
        self.comboBoxChipSelect.currentIndexChanged.connect(self.chipSelect)
        comPort = []
        for x in range(1,30):
            comPort.append('COM'+str(x))
        self.comboBoxCOMPort.addItems(comPort)
        self.comboBoxCOMPort.currentIndexChanged.connect(self.comPortSelect)
        self.comboBoxMemory.addItems(self.memoryESP32)
        self.comboBoxMemory.currentIndexChanged.connect(self.memorySelect)


    def memorySelect(self):
        self.flasSize = self.comboBoxMemory.currentText()


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
            self.labelBootloader.setText('Bootlader')
            self.pushButtonPartition.setEnabled(True)
            self.pushButtonApplication.setEnabled(True)
            self.comboBoxMemory.clear()
            self.comboBoxMemory.addItems(self.memoryESP32)


    def erase(self):

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

def main():
    app = QtGui.QApplication(sys.argv)
    windows = ESPToolGUIApp()
    windows.show()
    app.exec_()

if __name__=='__main__':
    main()
