# -*- coding: utf-8 -*-

"""
Module implementing TabWidget.
"""

from PyQt4.QtGui import QTabWidget
from PyQt4.QtCore import pyqtSignature
from Ui_gui import Ui_TabWidget
from PyQt4 import QtGui, QtCore
import time

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
        
        self.setCurrentIndex(0) # iniciar en tab home
        self.setWindowIcon(QtGui.QIcon('Trainer_16.png'))
        self.label.setText("<font color='white'>IN</font>")
        
        self.scene=QtGui.QGraphicsScene(self)
        self.scene.setSceneRect(QtCore.QRectF(0, 0, 460, 360))
        self.graphicsView.setScene(self.scene) #asignar scene al qgraphview
        self.home = QtGui.QGraphicsScene(self)
        self.graphicsView_2.setScene(self.home)
        #circulos
        self.r = 120
        self.x1 = 171.5 + self.r/2.0
        self.y1 = 50 + self.r/2.0
        self.x2 = 186.5 + self.r/2.0
        self.y2 = 65 + self.r/2.0
        self.circulos(self.r, self.x1, self.x2, self.y1, self.y2) # crear circulos
        #------------------------------------------------------------------------------------------------------
        # adding by emitting signal in different thread
        self.threadPool = []
        self.threadPool.append( WorkThread() )
        self.connect( self.threadPool[len(self.threadPool)-1], QtCore.SIGNAL("update(QString)"), self.showTime )
        self.temporizadorHome = 180 # segundos = 3min
        self.temporizadorTrain =  300 # segundo = 5 min
        self.segundosCirculo =0
        # Crear Timer para gestionar el radio del circulo
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.updateR)
        
        self.center()
    # metodo para centrar la ventana en la pantalla
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def circulos(self, r , x1, x2, y1, y2):    
        #Funcion para crear los circulos
        self.circulo1 = QtGui.QGraphicsEllipseItem(self.x1-(self.r/2.0), self.y1-(self.r/2.0), self.r, self.r)
        self.circulo1.setPen(QtGui.QColor(232, 232, 231))
        self.circulo1.setBrush(QtGui.QColor(232, 232, 231))
        self.scene.addItem(self.circulo1)
        self.circulo2 = QtGui.QGraphicsEllipseItem(self.x2-(self.r/2.0), self.y2-(self.r/2.0), self.r-30, self.r-30)
        self.circulo2.setBrush(QtGui.QColor(246, 245, 245))
        self.circulo2.setPen(QtGui.QColor(246, 245, 245))
        self.scene.addItem(self.circulo2)
        
    def updateR(self):
        self.scene.clear()
        #print "Segundos C: ", self.segundosCirculo
        if self.segundosCirculo <= 5:
            self.r += 2
            self.label.setText("<font color='black'>IN</font>")
            self.graphicsView.setBackgroundBrush(QtGui.QColor(15, 161, 239))
        elif self.segundosCirculo >5 and self.segundosCirculo <=7 :
            self.label.setText("<font color='black'>HOLD</font>")
            self.graphicsView.setBackgroundBrush(QtGui.QColor(255, 190, 160))
        elif  self.segundosCirculo >7 and self.segundosCirculo <=12:
            self.r -= 2
            self.label.setText("<font color='black'>OUT</font>")
            self.graphicsView.setBackgroundBrush(QtGui.QColor(239, 226, 62))

        if self.segundosCirculo == 13:
                self.segundosCirculo = 1
                self.r = 120
                self.it = 0
            
        self.circulos(self.r, self.x1, self.x2, self.y1, self.y2)    
    
    @pyqtSignature("")
    def on_stop_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.tab1.setEnabled(True)
        self.timer.stop()        
        self.temporizador2.setText("5:00")
        self.temporizadorTrain = 300
        self.threadPool[len(self.threadPool)-1].terminate() # parar thread
    
    @pyqtSignature("")
    def on_start_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.tab1.setEnabled(False)
        self.timerFlag =1
        self.temporizador2.setText("5:00")
        self.threadPool[len(self.threadPool)-1].start()
        
        self.timer.start(100)
        self.label.setText("<font color='white'>IN</font>")
        self.graphicsView.setBackgroundBrush(QtGui.QColor(15, 161, 239))
    
    @pyqtSignature("")
    def on_skipHome_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.tab2.setEnabled(True)
        self.setCurrentIndex(1) #cambiar de tab
        
     
    def showTime(self):
        
        if self.timerFlag==0:
                    #temporizador 
            minutes = int(self.temporizadorHome/60)
            seconds = int(self.temporizadorHome%60)
            if self.temporizadorHome < 0 : 
                self.threadPool[len(self.threadPool)-1].terminate() # parar thread
                self.temporizadorHome = 180
                self.stopHome.setEnabled(False)
                self.startHome.setEnabled(True)
                self.tab2.setEnabled(True)
                time.sleep(0.2)
                self.setCurrentIndex(self.currentIndex() + 1) #cambiar de tab
                print "Calibracion acabo"
            
            self.temporizadorHome -= 1   
            self.temporizador1.setText('%01d:%02d' % (minutes, seconds))   
            
        elif self.timerFlag==1:
            #temporizador 
            self.segundosCirculo +=1
            minutes = int(self.temporizadorTrain/60)
            seconds = int(self.temporizadorTrain%60)
            self.temporizadorTrain -= 1   
            self.temporizador2.setText('%01d:%02d' % (minutes, seconds))       
            if self.temporizadorTrain < 0 : 
                self.threadPool[len(self.threadPool)-1].terminate() # parar thread
                self.timer.stop()
                self.temporizadorTrain = 300
                print "Entrenamiento Acabo"


    
    @pyqtSignature("")
    def on_startHome_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.timerFlag = 0
        self.threadPool[len(self.threadPool)-1].start()
        self.startHome.setEnabled(False)
        self.skipHome.setEnabled(False)
        self.stopHome.setEnabled(True)
        self.temporizador1.setText("3:00") # reiniciar temporizador
    
    @pyqtSignature("")
    def on_stopHome_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.threadPool[len(self.threadPool)-1].terminate() # parar thread
        self.startHome.setEnabled(True)
        self.stopHome.setEnabled(False)
        self.skipHome.setEnabled(True)
        self.temporizador1.setText("3:00") # reiniciar temporizador
        self.temporizadorHome = 180 # reiniciar contador temporizador 
        
class WorkThread(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)
        global i
        i=0
    def __del__(self):
        self.wait()
 
    def run(self):
        while True:
            self.emit( QtCore.SIGNAL('update(QString)'), " ")  
            time.sleep(1) # artificial time delay
        return
                
