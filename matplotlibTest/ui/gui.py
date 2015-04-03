# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QMainWindow
from .Ui_gui import Ui_MainWindow
from .Ui_gui import *
import random

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
        self.plotButton.clicked.connect(self.PlotFunc) #
 
    def PlotFunc(self):
        randomNumbers = random.sample(range(0, 10), 10)
        self.widget.canvas.ax.clear()
        self.widget.canvas.ax.plot(randomNumbers)
        self.widget.canvas.draw()
        
