# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timer.ui'
#
# Created: Sun Dec 14 18:51:01 2008
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(527, 204)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.constant = QtGui.QPushButton(self.centralwidget)
        self.constant.setObjectName("constant")
        self.gridLayout.addWidget(self.constant, 0, 0, 1, 1)
        self.constantProgress = QtGui.QProgressBar(self.centralwidget)
        self.constantProgress.setProperty("value", QtCore.QVariant(0))
        self.constantProgress.setObjectName("constantProgress")
        self.gridLayout.addWidget(self.constantProgress, 0, 1, 1, 1)
        self.single = QtGui.QPushButton(self.centralwidget)
        self.single.setObjectName("single")
        self.gridLayout.addWidget(self.single, 1, 0, 1, 1)
        self.singleProgress = QtGui.QProgressBar(self.centralwidget)
        self.singleProgress.setProperty("value", QtCore.QVariant(0))
        self.singleProgress.setObjectName("singleProgress")
        self.gridLayout.addWidget(self.singleProgress, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 527, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.constant.setText(QtGui.QApplication.translate("MainWindow", "Constant Timer", None, QtGui.QApplication.UnicodeUTF8))
        self.single.setText(QtGui.QApplication.translate("MainWindow", "SingleShot Timer", None, QtGui.QApplication.UnicodeUTF8))

