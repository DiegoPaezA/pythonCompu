# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

#from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QMainWindow

from .Ui_guide import Ui_MainWindow


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
