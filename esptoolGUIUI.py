# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'esptoolGUI.ui'
#
# Created: Wed Mar 01 12:01:10 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class ComboBoxCOMPORT(QtWidgets.QComboBox):
    popupAboutToBeShown = QtCore.pyqtSignal()

    def showPopup(self):
        self.popupAboutToBeShown.emit()
        super(ComboBoxCOMPORT, self).showPopup()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 640)
        #MainWindow.setMinimumSize(QtCore.QSize(444, 294))
        #MainWindow.setMaximumSize(QtCore.QSize(444, 294))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("espLogo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 441, 291))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        #self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.labelBootloader = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelBootloader.setObjectName(_fromUtf8("labelBootloader"))
        self.labelBootloader.setText("bootloader.bin")
        self.verticalLayout_2.addWidget(self.labelBootloader)
        self.labelPartition = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelPartition.setObjectName(_fromUtf8("labelPartition"))
        self.labelPartition.setText("partitions.bin")
        self.verticalLayout_2.addWidget(self.labelPartition)
        self.labelApplication = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelApplication.setObjectName(_fromUtf8("labelApplication"))
        self.verticalLayout_2.addWidget(self.labelApplication)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.pushButtonBootloader = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonBootloader.setObjectName(_fromUtf8("pushButtonBootloader"))
        self.verticalLayout_4.addWidget(self.pushButtonBootloader)
        self.pushButtonPartition = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonPartition.setObjectName(_fromUtf8("pushButtonPartition"))
        self.verticalLayout_4.addWidget(self.pushButtonPartition)
        self.pushButtonApplication = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonApplication.setObjectName(_fromUtf8("pushButtonApplication"))
        self.verticalLayout_4.addWidget(self.pushButtonApplication)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.comboBoxBaudSelect = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBoxChipSelect = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBoxBaudSelect.setObjectName(_fromUtf8("comboBoxBaudSelect"))
        self.horizontalLayout_3.addWidget(self.comboBoxChipSelect)
        self.horizontalLayout_3.addWidget(self.comboBoxBaudSelect)
        self.comboBoxCOMPort = ComboBoxCOMPORT(self.verticalLayoutWidget)
        self.comboBoxCOMPort.setObjectName(_fromUtf8("comboBoxCOMPort"))
        self.horizontalLayout_3.addWidget(self.comboBoxCOMPort, QtCore.Qt.AlignHCenter)
        self.comboBoxMemory = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBoxMemory.setObjectName(_fromUtf8("comboBoxMemory"))
        self.horizontalLayout_3.addWidget(self.comboBoxMemory)
        self.pushButtonErase = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonErase.setObjectName(_fromUtf8("pushButtonErase"))
        self.horizontalLayout_3.addWidget(self.pushButtonErase)
        self.pushButtonFlashAll = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonFlashAll.setObjectName(_fromUtf8("pushButtonFlashAll"))
        self.horizontalLayout_3.addWidget(self.pushButtonFlashAll)		
        self.pushButtonFlashBoot = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonFlashBoot.setObjectName(_fromUtf8("pushButtonFlashBoot"))
        self.horizontalLayout_3.addWidget(self.pushButtonFlashBoot)
        self.pushButtonFlash = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonFlash.setObjectName(_fromUtf8("pushButtonFlash"))
        self.horizontalLayout_3.addWidget(self.pushButtonFlash)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_5)
        self.plainTextEditStatus = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEditStatus.setEnabled(True)
        self.plainTextEditStatus.setAcceptDrops(False)
        self.plainTextEditStatus.setUndoRedoEnabled(False)
        self.plainTextEditStatus.setReadOnly(True)
        self.plainTextEditStatus.setObjectName(_fromUtf8("plainTextEditStatus"))
		
        self.comboBoxCmd = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBoxCmd.setObjectName(_fromUtf8("comboBoxCmd"))
        self.comboBoxCmd.setEditable(True)
        self.pushButtonSend = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonSend.setObjectName(_fromUtf8("pushButtonSend"))
        self.pushButtonOpen = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonOpen.setObjectName(_fromUtf8("pushButtonOpen"))
        self.pushButtonClose = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonClose.setObjectName(_fromUtf8("pushButtonClose"))
        self.pushButtonClear = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonClear.setObjectName(_fromUtf8("pushButtonClear"))
		
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.horizontalLayout_4.addWidget(self.comboBoxCmd, QtCore.Qt.AlignLeft)
        self.horizontalLayout_4.addWidget(self.pushButtonSend )
        self.horizontalLayout_4.addWidget(self.pushButtonOpen )
        self.horizontalLayout_4.addWidget(self.pushButtonClose )
        self.horizontalLayout_4.addWidget(self.pushButtonClear )

        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.verticalLayout_6)
		
        self.verticalLayout.addWidget(self.plainTextEditStatus)		
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ESP32 Flash Tool - PyQt5", None))
        self.labelBootloader.setText(_translate("MainWindow", "bootloader.bin", None))
        self.labelPartition.setText(_translate("MainWindow", "partitions.bin", None))
        self.labelApplication.setText(_translate("MainWindow", "", None))
        self.pushButtonBootloader.setText(_translate("MainWindow", "Bootloade&r", None))
        self.pushButtonPartition.setText(_translate("MainWindow", "Partitio&n", None))
        self.pushButtonApplication.setText(_translate("MainWindow", "Firm&ware", None))

        self.pushButtonErase.setVisible(False)
        self.pushButtonErase.setText(_translate("MainWindow", "Erase", None))
        self.pushButtonFlashAll.setText(_translate("MainWindow", "Flash &All", None))
        self.pushButtonFlashBoot.setText(_translate("MainWindow", "Flash &Boot Loader", None))
        self.pushButtonFlash.setText(_translate("MainWindow", "Flash &Firmware", None))

        self.pushButtonSend.setText(_translate("MainWindow", "&Send", None))
        self.pushButtonOpen.setText(_translate("MainWindow", "&Open", None))
        self.pushButtonClose.setText(_translate("MainWindow", "&Close", None))
        self.pushButtonClear.setText(_translate("MainWindow", "Clear &Log", None))		