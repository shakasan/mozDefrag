# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mozDefragMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(395, 383)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Belgium))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logo_header = QtWidgets.QLabel(self.centralwidget)
        self.logo_header.setGeometry(QtCore.QRect(0, 0, 400, 115))
        self.logo_header.setText("")
        self.logo_header.setPixmap(QtGui.QPixmap(":/pictures/pic/logo_header.jpg"))
        self.logo_header.setObjectName("logo_header")
        self.aboutButton = QtWidgets.QPushButton(self.centralwidget)
        self.aboutButton.setGeometry(QtCore.QRect(10, 340, 112, 31))
        self.aboutButton.setObjectName("aboutButton")
        self.defragAllButton = QtWidgets.QPushButton(self.centralwidget)
        self.defragAllButton.setGeometry(QtCore.QRect(270, 340, 112, 31))
        self.defragAllButton.setDefault(False)
        self.defragAllButton.setObjectName("defragAllButton")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 130, 141, 80))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBoxThunderbird = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBoxThunderbird.setObjectName("checkBoxThunderbird")
        self.verticalLayout.addWidget(self.checkBoxThunderbird)
        self.checkBoxFirefoxTrunk = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBoxFirefoxTrunk.setEnabled(True)
        self.checkBoxFirefoxTrunk.setObjectName("checkBoxFirefoxTrunk")
        self.verticalLayout.addWidget(self.checkBoxFirefoxTrunk)
        self.checkBoxFirefox = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBoxFirefox.setEnabled(True)
        self.checkBoxFirefox.setObjectName("checkBoxFirefox")
        self.verticalLayout.addWidget(self.checkBoxFirefox)
        self.logTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.logTextEdit.setGeometry(QtCore.QRect(10, 220, 371, 111))
        self.logTextEdit.setReadOnly(True)
        self.logTextEdit.setObjectName("logTextEdit")
        self.logo_header.raise_()
        self.aboutButton.raise_()
        self.defragAllButton.raise_()
        self.logTextEdit.raise_()
        self.layoutWidget.raise_()
        self.logTextEdit.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "mozDefrag"))
        self.aboutButton.setText(_translate("MainWindow", "About"))
        self.defragAllButton.setText(_translate("MainWindow", "Defrag"))
        self.checkBoxThunderbird.setText(_translate("MainWindow", "Thunderbird"))
        self.checkBoxFirefoxTrunk.setText(_translate("MainWindow", "Firefox Nightly"))
        self.checkBoxFirefox.setText(_translate("MainWindow", "Firefox"))

import res_pics_rc
