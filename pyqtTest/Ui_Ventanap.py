__author__ = 'diegopaez'
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/diripar8/Developer/web/ui/Ventanap.ui'
#
# Created: Tue Sep 23 20:29:34 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(440, 295)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.ir = QtGui.QPushButton(self.centralWidget)
        self.ir.setGeometry(QtCore.QRect(9, 9, 85, 31))
        self.ir.setObjectName(_fromUtf8("ir"))
        self.txt = QtGui.QLineEdit(self.centralWidget)
        self.txt.setGeometry(QtCore.QRect(100, 9, 146, 31))
        self.txt.setObjectName(_fromUtf8("txt"))
        self.webView = QtWebKit.QWebView(self.centralWidget)
        self.webView.setGeometry(QtCore.QRect(10, 60, 411, 131))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.ok = QtGui.QPushButton(self.centralWidget)
        self.ok.setGeometry(QtCore.QRect(10, 200, 91, 31))
        self.ok.setObjectName(_fromUtf8("ok"))
        self.outLabel = QtGui.QLabel(self.centralWidget)
        self.outLabel.setGeometry(QtCore.QRect(170, 210, 81, 21))
        self.outLabel.setText(_fromUtf8(""))
        self.outLabel.setObjectName(_fromUtf8("outLabel"))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.ir.setText(QtGui.QApplication.translate("MainWindow", "ir", None, QtGui.QApplication.UnicodeUTF8))
        self.ok.setText(QtGui.QApplication.translate("MainWindow", "TEST", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

