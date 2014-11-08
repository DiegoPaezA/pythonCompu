# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
from PyQt4 import QtCore, QtGui
import sys, time

from Ui_home import Ui_MainWindow


def suma (a, b):
    print a + b



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
        self.i=0
        self.center() # Centra la ventana en la pantalla
        self.ButtonStart.clicked.connect(self.start)
        self.ButtonStop.clicked.connect(self.stop)
    
      # metodo para centrar la ventana en la pantalla
    def center(self):        
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def start(self):
    
        self.i == 0 
        print "ok"
            
    def stop(self):
        self.i == 1    
