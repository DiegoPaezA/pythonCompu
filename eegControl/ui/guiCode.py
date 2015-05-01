# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QMainWindow

from .Ui_gui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        #self.plotButton.clicked.connect(self.plotGraph)
    
    @pyqtSignature("")
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        print "hola mundo"
        # TODO: not implemented yet
        #raise NotImplementedError
