# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/diegopaez/PycharmProjects/controlDeportivo/ui/home.ui'
#
# Created: Tue Nov  4 13:02:08 2014
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
        MainWindow.resize(483, 247)
        MainWindow.setAutoFillBackground(False)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.ButtonStart = QtGui.QPushButton(self.centralWidget)
        self.ButtonStart.setGeometry(QtCore.QRect(9, 50, 99, 26))
        self.ButtonStart.setObjectName(_fromUtf8("ButtonStart"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(166, 9, 176, 33))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Mukti Narrow"))
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.ButtonTrigeron = QtGui.QPushButton(self.centralWidget)
        self.ButtonTrigeron.setGeometry(QtCore.QRect(9, 114, 123, 26))
        self.ButtonTrigeron.setObjectName(_fromUtf8("ButtonTrigeron"))
        self.ButtonStop = QtGui.QPushButton(self.centralWidget)
        self.ButtonStop.setGeometry(QtCore.QRect(9, 82, 96, 26))
        self.ButtonStop.setObjectName(_fromUtf8("ButtonStop"))
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(166, 82, 75, 15))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(166, 50, 23, 15))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.labelbpsout = QtGui.QLabel(self.centralWidget)
        self.labelbpsout.setGeometry(QtCore.QRect(250, 50, 58, 16))
        self.labelbpsout.setObjectName(_fromUtf8("labelbpsout"))
        self.labelintervaloRR = QtGui.QLabel(self.centralWidget)
        self.labelintervaloRR.setGeometry(QtCore.QRect(250, 80, 58, 16))
        self.labelintervaloRR.setObjectName(_fromUtf8("labelintervaloRR"))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.ButtonStart.setText(_translate("MainWindow", "Start Capture", None))
        self.label.setText(_translate("MainWindow", "Interface de Controle", None))
        self.ButtonTrigeron.setText(_translate("MainWindow", "Trigger Shot Start", None))
        self.ButtonStop.setText(_translate("MainWindow", "Stop Capture", None))
        self.label_3.setText(_translate("MainWindow", "Intervalo RR", None))
        self.label_2.setText(_translate("MainWindow", "bps", None))
        self.labelbpsout.setText(_translate("MainWindow", "TextLabel", None))
        self.labelintervaloRR.setText(_translate("MainWindow", "TextLabel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

