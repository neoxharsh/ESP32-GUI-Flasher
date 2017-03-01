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
        self.initButtons()
        self.initProcess()
        self.baudRate = 921600
        self.port = 'COM'
        self.flasSize = '4M'
        self.frozen = 'not'


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
        self.lineEditMemory.setDisabled(True)
        self.lineEditCOMPort.setDisabled(True)
        self.comboBoxBaudSelect.setDisabled(True)

    def enableButtons(self):
        self.pushButtonErase.setDisabled(False)
        self.pushButtonFlash.setDisabled(False)
        self.pushButtonPartition.setDisabled(False)
        self.pushButtonBootloader.setDisabled(False)
        self.pushButtonApplication.setDisabled(False)
        self.lineEditMemory.setDisabled(False)
        self.lineEditCOMPort.setDisabled(False)
        self.comboBoxBaudSelect.setDisabled(False)

    def initButtons(self):
        self.pushButtonBootloader.clicked.connect(lambda: self.selectFile('Select Bootloader File',self.labelBootloader))
        self.pushButtonPartition.clicked.connect(lambda: self.selectFile('Select Partition File',self.labelPartition))
        self.pushButtonApplication.clicked.connect(lambda: self.selectFile('Select Application File',self.labelApplication))
        self.pushButtonFlash.clicked.connect(self.flash)
        self.pushButtonErase.clicked.connect(self.erase)

        self.comboBoxBaudSelect.addItems(['921600','512000','256000','230400','115200'])
        self.comboBoxBaudSelect.currentIndexChanged.connect(self.baudSelect)

        self.lineEditMemory.textChanged.connect(self.flashSizeSelect)
        self.lineEditCOMPort.textChanged.connect(self.portSelect)

    def erase(self):
        if (os.name=='nt'):
            self.process.start(self.bundle_dir+'/esptool.exe --chip esp32 --port {0} --baud {1} erase_flash'.format(self.port,self.baudRate))
        else:
            self.process.start(self.bundle_dir+'/python esptool.py --chip esp32 --port {0} --baud {1} erase_flash'.format(self.port,self.baudRate))


    def flash(self):
        if (os.name=='nt'):

            self.process.start(self.bundle_dir+'/esptool.exe --chip esp32 --port {0} --baud {1}\
                            --before default_reset --after hard_reset write_flash\
                            -z --flash_freq 80m --flash_mod dio --flash_size {2} \
                             0x1000 {3} 0x8000 {4} 0x10000 {5}'.format(self.port,self.baudRate,self.flasSize,self.labelBootloader.text(),self.labelPartition.text(),self.labelApplication.text()))
        else:
            self.process.start(self.bundle_dir+'/python esptool.py --chip esp32 --port {0} --baud {1}\
                            --before default_reset --after hard_reset write_flash\
                            -z --flash_freq 80m --flash_mod dio --flash_size {2} \
                             0x1000 {3} 0x8000 {4} 0x10000 {5}'.format(self.port,self.baudRate,self.flasSize,self.labelBootloader.text(),self.labelPartition.text(),self.labelApplication.text()))

def main():
    app = QtGui.QApplication(sys.argv)
    windows = ESPToolGUIApp()
    windows.show()
    app.exec_()

if __name__=='__main__':
    main()
