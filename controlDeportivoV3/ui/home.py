# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
from PyQt4 import QtCore, QtGui
import sys, time


import numpy as np
import os

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
        
        self.buttongo.clicked.connect(self.enablebuttons)
        self.ButtonStart.clicked.connect(self.start)
        self.ButtonStop.clicked.connect(self.stop)
        
        self.plotButton.clicked.connect(self.plotGraph)
        
        # Radioboton 
        #self.activarVFC.setChecked(True)
        #self.activarEMG.setChecked(False)
        
        self.tiempo = QtCore.QTime()
        
        # crear timer
        #Creo mi Timer y lo conecto a una funcion
        self.ctimer = QtCore.QTimer()
        QtCore.QObject.connect(self.ctimer, QtCore.SIGNAL("timeout()"), self.readADC)
        self.ctimer.setInterval(100)
        
        # adding by emitting signal in different thread
        self.threadPool = []
        self.threadPool.append( WorkThread() )
        self.connect( self.threadPool[len(self.threadPool)-1], QtCore.SIGNAL("update(QString)"), self.showTime )
        
        

        self.p =self.plot 
        
        self.curve1 = self.p.plot()
        
        
      # metodo para centrar la ventana en la pantalla
    def center(self):        
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
     # metodo thread
  #  def threadLoop(self):
         
         
         

    def start(self):
    
        print "Funcion Start : " ,  self.dataread
        
        #self.ctimer.start()
        #self.threadPool[len(self.threadPool)-1].start()
        
        #self.temporizador = 180 # segundos
        #self.tempoProva = 0

            
    def stop(self):
        
        self.ButtonStart.setEnabled(False)
        self.ButtonStop.setEnabled(False)
        self.ButtonTrigeron.setEnabled(False)
        self.Readtext.clear()  
        self.Readtext.setEnabled(True) 
        
        #self.threadPool[len(self.threadPool)-1].terminate() # parar thread
        self.totalrr = np.random.randint(10, size=10)
        
        np.savetxt('rr' + str(self.dataread)  + '.txt', self.totalrr, fmt='%i') # salvar archivo rr total
        os.chdir(self.directorioOriginal) # vuelve al directorio inicial
        #self.ctimer.stop() # parar timer
        
        
        
    def enablebuttons(self):
        i = 1  
        self.dataread = self.Readtext.text()
        self.crearDir() ## crear directorio
        
        if self.dataread == "":
            print "Ingrese el nombre y numero de la prueba test1"
            msgBox = QtGui.QMessageBox()
            msgBox.setText('  Insira o Nome + Numero do Teste.  ')
            msgBox.setInformativeText("       Exemplo: teste1hiago ")
            msgBox.setWindowTitle ('Warning!')
            msgBox.addButton(QtGui.QPushButton('Ok'), QtGui.QMessageBox.AcceptRole)
            ret = msgBox.exec_();
           
        else:
            print "habilite los botones"
            self.ButtonStart.setEnabled(True)
            self.ButtonStop.setEnabled(True)
            self.ButtonTrigeron.setEnabled(True)
            self.Readtext.clear()  
            self.Readtext.setEnabled(False)
    


    def showTime(self):
    #Show Current Time in "hh:mm:ss" format
        b = self.tiempo.currentTime().toString(str("hh:mm:ss"))
        
        #temporizador 
        minutes = int(self.temporizador/60)
        seconds = int(self.temporizador%60)
          
        # print('%02d:%02d' % (minutes, seconds))
        
        # tiempo prueba
        minutesP = int(self.tempoProva/60)
        secondsP = int(self.tempoProva%60)
          
        #print('%02d:%02d' % (minutesP, secondsP))
        
        self.temporizador -= 1
        self.tempoProva += 1
        
        if self.temporizador == 0 : 
            self.temporizador = 180
            print "Teste Acabo"
            
        self.relojout.setText('%02d:%02d' % (minutes, seconds))
        self.tempoProvaout.setText('%02d:%02d' % (minutesP, secondsP))
        #print self.tiempo.currentTime()
        


    def crearDir(self):
        self.directorioOriginal = os.getcwd()
        carpeta = "controlDeportivoV3/" +  str(self.dataread)

        directorio = os.path.join(os.pardir, carpeta)
        if not os.path.isdir(directorio):
            os.mkdir(directorio)
        os.chdir(directorio)

        
    def readADC(self):
    #Show Current Time in "hh:mm:ss" format
        print "ADC Read"
        
    def plotGraph(self):

        if self.plotEMG.isChecked() : 
            print "plot emg"
        elif self.plotVFC.isChecked() :
            print "plot VFC"
    
    @pyqtSignature("")
    def on_resetButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
        
       

class WorkThread(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)
        global i
        i=0
    def __del__(self):
        self.wait()
 
    def run(self):
        while i==0:
            self.emit( QtCore.SIGNAL('update(QString)'), " ")  
            time.sleep(1) # artificial time delay
        return
  

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())



