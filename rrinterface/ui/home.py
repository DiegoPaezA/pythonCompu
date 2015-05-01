# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
from PyQt4 import QtCore, QtGui
import sys, time


import numpy as np
import pyqtgraph as pg

from Ui_home import Ui_MainWindow



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

        self.setWindowTitle("Interface de Control")
        self.center() # Centra la ventana en la pantalla
        
        #self.buttongo.clicked.connect(self.enablebuttons)
        #self.ButtonStart.clicked.connect(self.start)
        #self.ButtonStop.clicked.connect(self.stop)
        
        self.plotButton.clicked.connect(self.plotGraph)
        
        self.tiempo = QtCore.QTime()
        
        # crear timer
        #Creo mi Timer y lo conecto a una funcion
        self.ctimer = QtCore.QTimer()
        QtCore.QObject.connect(self.ctimer, QtCore.SIGNAL("timeout()"), self.readADC)
        self.ctimer.setInterval(100)
       
        self.p =self.plot 
        self.curve1 = self.p.plot()
        
        
    # metodo para centrar la ventana en la pantalla
    def center(self):        
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    
    def start(self):
        print "start ok"
            
    def stop(self):
 
        print "stop ok"
        

    def readADC(self):
    #Show Current Time in "hh:mm:ss" format
        print "ADC Read"
        
    def plotGraph(self):
        
        print "Plot Graph"
        a = np.random.rand(20)
        self.curve1.setData(a,pen=(200,200,200), symbolBrush=(255,0,0), symbolPen='w', symbolSize = 4)
    
    @pyqtSignature("")
    def on_ButtonStart_clicked(self):
        """
        Slot documentation goes here.
        """
        print "Hola Mundo"
