from PyQt4 import QtGui, QtCore
import sys


class MicroGravedad(QtCore.QObject):

    def __init__(self):
        super(MicroGravedad, self).__init__()
        
        # Crear Timer
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.ReadImu)
        self.timer.start(500)
        self.i = 0

    def ReadImu(self):
        print "Leer Imu"
        self.i += 1
        if self.i > 10:
            #QtCore.QCoreApplication.instance().quit()
            QtCore.QCoreApplication.exit(0)


    def keyPressEvent(self, evento):
    	print "evento teclado"
    	self.timer.start(500)




if __name__ == "__main__":
    
    app = QtCore.QCoreApplication(sys.argv)
    micro = MicroGravedad()
    sys.exit(app.exec_())