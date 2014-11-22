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

        self.setWindowTitle("Interface de Control")
        self.center() # Centra la ventana en la pantalla
        
        self.buttongo.clicked.connect(self.enablebuttons)
        self.ButtonStart.clicked.connect(self.start)
        self.ButtonStop.clicked.connect(self.stop)
        
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
        
      # metodo para centrar la ventana en la pantalla
    def center(self):        
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
     # metodo thread
  #  def threadLoop(self):
         
         
         

    def start(self):
    

        print "ok"
        shost = self.Readtext.text()
        print shost
        #self.ctimer.start()
        self.threadPool[len(self.threadPool)-1].start()
       
            
    def stop(self):
 
        self.ButtonStart.setEnabled(False)
        self.ButtonStop.setEnabled(False)
        self.ButtonTrigeron.setEnabled(False)
        self.Readtext.clear()  
        self.Readtext.setEnabled(True) 
        
        self.threadPool[len(self.threadPool)-1].terminate()
        
        #self.ctimer.stop()
        
        #msgBox = QtGui.QMessageBox()
        #msgBox.setText('  Insira o Nome + Numero do Teste.  ')
        #msgBox.setInformativeText("       Exemplo: teste2hiago ")
        #msgBox.setWindowTitle ('Warning!')
        #msgBox.addButton(QtGui.QPushButton('Ok'), QtGui.QMessageBox.AcceptRole)
        #ret = msgBox.exec_();
        
        
    def enablebuttons(self):
        i = 1  
        dataread = self.Readtext.text()

        if dataread == "":
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
        #self.display(QTime.currentTime().toString(QString("hh:mm:ss")))
        a =  self.tiempo.currentTime()
        b = self.tiempo.currentTime().toString(str("hh:mm:ss"))
        

        print b
        self.relojout.setText(b)
        #print self.tiempo.currentTime()
    
    def readADC(self):
    #Show Current Time in "hh:mm:ss" format
        print "Read ADC"
    

class WorkThread(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)
        global i
        i=0
    def __del__(self):
        self.wait()
 
    def run(self):
        #for i in range(6):
        #time.sleep(0.3) # artificial time delay
        #self.emit( QtCore.SIGNAL('update(QString)'), "from work thread " + str(i) )

        while i==0:
            self.emit( QtCore.SIGNAL('update(QString)'), "from work thread " + str(i) )  
            time.sleep(1) # artificial time delay 
            print "ok--"
        return
  

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()

    sys.exit(app.exec_())



