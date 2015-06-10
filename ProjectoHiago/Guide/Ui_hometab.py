# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ieb-ufsc/PycharmProjects/ProjectoHiago/Guide/hometab.ui'
#
# Created: Wed Jun 10 14:27:49 2015
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

class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName(_fromUtf8("TabWidget"))
        TabWidget.setEnabled(True)
        TabWidget.resize(459, 364)
        TabWidget.setMouseTracking(False)
        TabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        TabWidget.setTabPosition(QtGui.QTabWidget.North)
        TabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        TabWidget.setElideMode(QtCore.Qt.ElideNone)
        TabWidget.setTabsClosable(False)
        TabWidget.setMovable(False)
        self.tab = QtGui.QWidget()
        self.tab.setEnabled(True)
        self.tab.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tab1 = QtGui.QPushButton(self.tab)
        self.tab1.setGeometry(QtCore.QRect(145, 110, 85, 26))
        self.tab1.setObjectName(_fromUtf8("tab1"))
        TabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setEnabled(True)
        self.tab_2.setMouseTracking(False)
        self.tab_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tab2 = QtGui.QPushButton(self.tab_2)
        self.tab2.setGeometry(QtCore.QRect(150, 110, 85, 26))
        self.tab2.setObjectName(_fromUtf8("tab2"))
        TabWidget.addTab(self.tab_2, _fromUtf8(""))

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        TabWidget.setWindowTitle(_translate("TabWidget", "TabWidget", None))
        self.tab1.setText(_translate("TabWidget", "PushButton", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab), _translate("TabWidget", "Home", None))
        self.tab2.setText(_translate("TabWidget", "PushButton", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_2), _translate("TabWidget", "Tab 2", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    TabWidget = QtGui.QTabWidget()
    ui = Ui_TabWidget()
    ui.setupUi(TabWidget)
    TabWidget.show()
    sys.exit(app.exec_())

