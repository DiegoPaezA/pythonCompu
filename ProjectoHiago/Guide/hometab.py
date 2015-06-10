# -*- coding: utf-8 -*-

"""
Module implementing TabWidget.
"""

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QTabWidget

from .Ui_hometab import Ui_TabWidget


class TabWidget(QTabWidget, Ui_TabWidget):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        QTabWidget.__init__(self, parent)
        self.setupUi(self)
    
    @pyqtSignature("")
    def on_tab1_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print "tab 1"
        self.setCurrentIndex(self.currentIndex() + 1) #cambiar de tab
    
    @pyqtSignature("")
    def on_tab2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print "tab 2"
        self.setCurrentIndex(self.currentIndex() - 1) #cambiar de tab atras    
