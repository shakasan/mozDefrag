#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
mozDefrag
Description : defrag Firefox/Thunderbird's sqlite databases for users/profiles
Author : Francois Beckers
Licence : GPL3
"""

import os
import sys
import mozDefragMainWindow
import mozDefragAboutWindow
import res_pics_rc
from libMozDefrag import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

__appVer__ = "0.1 alpha"
__appDir__ = "/opt/mozdefrag/"


class Ui_mozDefragAboutWindow(QtWidgets.QMainWindow,  # --- About -------------
                              mozDefragAboutWindow.Ui_AboutWindow):

    def __init__(self, parent=None):
        super(Ui_mozDefragAboutWindow, self).__init__(parent)
        self.setupUi(self)
        self.connectActions()
        self.setWindowTitle("About mozDefrag " + __appVer__)

    def connectActions(self):
        self.closeButton.clicked.connect(self.close)


class Ui_mozDefragMainWindow(QtWidgets.QMainWindow,  # --- Main ---------------
                             mozDefragMainWindow.Ui_MainWindow):

    def __init__(self, parent=None):
        super(Ui_mozDefragMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.connectActions()

    def connectActions(self):
        self.aboutButton.clicked.connect(self.showMozDefragAboutWindow)
        self.defragAllButton.clicked.connect(self.performDefrag)

    def showMozDefragAboutWindow(self):
        self.child_win = Ui_mozDefragAboutWindow(self)
        self.child_win.show()

    def performDefrag(self):
        if self.checkBoxFirefox.isChecked():
            if not mozFirefoxIsRunning():
                mozDefragFirefox()
                self.logTextEdit.append("> Firefox defrag done")
            else:
                self.logTextEdit.append("> Close Firefox and try again")
        if self.checkBoxThunderbird.isChecked():
            if not mozThunderbirdIsRunning():
                mozDefragThunderbird()
                self.logTextEdit.append("> Thunderbird defrag done")
            else:
                self.logTextEdit.append("> Close Thunderbird and try again")

    def main(self):
        self.show()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/pic/icon.svg"),
                                     QtGui.QIcon.Normal,
                                     QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setWindowTitle("mozDefrag " + __appVer__)
        if mozFirefoxIsInstalled():
            self.checkBoxFirefox.setEnabled(True)
            self.checkBoxFirefox.setChecked(True)
        else:
            self.checkBoxFirefox.setDisabled(True)
        if mozThunderbirdIsInstalled():
            self.checkBoxThunderbird.setEnabled(True)
            self.checkBoxThunderbird.setChecked(True)
        else:
            self.checkBoxThunderbird.setDisabled(True)


if __name__ == '__main__':  # --- app init ------------------------------------

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = Ui_mozDefragMainWindow()
    mainWindow.main()
    app.exec_()
