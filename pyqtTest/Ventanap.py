# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature,  QUrl

from Ui_Ventanap import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
    
    @pyqtSignature("")
    def on_ir_released(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.webView.setUrl(QUrl(self.txt.text()))
        #raise NotImplementedError
    
    @pyqtSignature("")
    def on_ok_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        a1 = "OK Click "
        self.outLabel.setText(a1)
        
        #raise NotImplementedError
    
    @pyqtSignature("")
    def on_ok_released(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        a2 = "OK Released "
        self.outLabel.setText(a2)

        #raise NotImplementedError
