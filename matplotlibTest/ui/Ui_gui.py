# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/diegopaez/PycharmProjects/matplotlibTest/ui/gui.ui'
#
# Created: Fri Apr  3 14:17:05 2015
#      by: PyQt4 UI code generator 4.10.4
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
        MainWindow.resize(800, 600)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.plotButton = QtGui.QPushButton(self.centralWidget)
        self.plotButton.setGeometry(QtCore.QRect(335, 40, 103, 28))
        self.plotButton.setObjectName(_fromUtf8("plotButton"))
        self.widget = MatplotlibWidget(self.centralWidget)
        self.widget.setGeometry(QtCore.QRect(55, 105, 686, 416))
        self.widget.setObjectName(_fromUtf8("widget"))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.plotButton.setText(_translate("MainWindow", "PLOT", None))

from matplotlibwidgetFile import MatplotlibWidget

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

