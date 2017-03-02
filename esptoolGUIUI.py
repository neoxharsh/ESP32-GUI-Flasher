# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'esptoolGUI.ui'
#
# Created: Wed Mar 01 12:01:10 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(444, 294)
        MainWindow.setMinimumSize(QtCore.QSize(444, 294))
        MainWindow.setMaximumSize(QtCore.QSize(444, 294))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("espLogo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 441, 291))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.labelBootloader = QtGui.QLabel(self.verticalLayoutWidget)
        self.labelBootloader.setObjectName(_fromUtf8("labelBootloader"))
        self.verticalLayout_2.addWidget(self.labelBootloader)
        self.labelPartition = QtGui.QLabel(self.verticalLayoutWidget)
        self.labelPartition.setObjectName(_fromUtf8("labelPartition"))
        self.verticalLayout_2.addWidget(self.labelPartition)
        self.labelApplication = QtGui.QLabel(self.verticalLayoutWidget)
        self.labelApplication.setObjectName(_fromUtf8("labelApplication"))
        self.verticalLayout_2.addWidget(self.labelApplication)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.pushButtonBootloader = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButtonBootloader.setObjectName(_fromUtf8("pushButtonBootloader"))
        self.verticalLayout_4.addWidget(self.pushButtonBootloader)
        self.pushButtonPartition = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButtonPartition.setObjectName(_fromUtf8("pushButtonPartition"))
        self.verticalLayout_4.addWidget(self.pushButtonPartition)
        self.pushButtonApplication = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButtonApplication.setObjectName(_fromUtf8("pushButtonApplication"))
        self.verticalLayout_4.addWidget(self.pushButtonApplication)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.comboBoxBaudSelect = QtGui.QComboBox(self.verticalLayoutWidget)
        self.comboBoxChipSelect = QtGui.QComboBox(self.verticalLayoutWidget)
        self.comboBoxBaudSelect.setObjectName(_fromUtf8("comboBoxBaudSelect"))
        self.horizontalLayout_3.addWidget(self.comboBoxChipSelect)
        self.horizontalLayout_3.addWidget(self.comboBoxBaudSelect)
        self.comboBoxCOMPort = QtGui.QComboBox(self.verticalLayoutWidget)
        self.comboBoxCOMPort.setObjectName(_fromUtf8("comboBoxCOMPort"))
        self.horizontalLayout_3.addWidget(self.comboBoxCOMPort, QtCore.Qt.AlignHCenter)
        self.comboBoxMemory = QtGui.QComboBox(self.verticalLayoutWidget)
        self.comboBoxMemory.setObjectName(_fromUtf8("comboBoxMemory"))
        self.horizontalLayout_3.addWidget(self.comboBoxMemory)
        self.pushButtonErase = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButtonErase.setObjectName(_fromUtf8("pushButtonErase"))
        self.horizontalLayout_3.addWidget(self.pushButtonErase)
        self.pushButtonFlash = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButtonFlash.setObjectName(_fromUtf8("pushButtonFlash"))
        self.horizontalLayout_3.addWidget(self.pushButtonFlash)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_5)
        self.plainTextEditStatus = QtGui.QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEditStatus.setEnabled(True)
        self.plainTextEditStatus.setAcceptDrops(False)
        self.plainTextEditStatus.setUndoRedoEnabled(False)
        self.plainTextEditStatus.setReadOnly(True)
        self.plainTextEditStatus.setObjectName(_fromUtf8("plainTextEditStatus"))
        self.verticalLayout.addWidget(self.plainTextEditStatus)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ESP Flash Tool", None))
        self.labelBootloader.setText(_translate("MainWindow", "Bootloader", None))
        self.labelPartition.setText(_translate("MainWindow", "Partition", None))
        self.labelApplication.setText(_translate("MainWindow", "Application", None))
        self.pushButtonBootloader.setText(_translate("MainWindow", "Bootloader", None))
        self.pushButtonPartition.setText(_translate("MainWindow", "Partition", None))
        self.pushButtonApplication.setText(_translate("MainWindow", "Application", None))

        self.pushButtonErase.setText(_translate("MainWindow", "Erase", None))
        self.pushButtonFlash.setText(_translate("MainWindow", "Flash", None))
