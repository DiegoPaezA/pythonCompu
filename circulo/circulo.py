import sys 
from PyQt4 import QtGui, QtCore

class MyView(QtGui.QGraphicsView):
    def __init__(self):
        QtGui.QGraphicsView.__init__(self)

        self.setGeometry(QtCore.QRect(100, 100, 600, 250))

        self.scene = QtGui.QGraphicsScene(self)
        self.scene.setSceneRect(QtCore.QRectF())

        self.setScene(self.scene)
	self.item = QtGui.QGraphicsEllipseItem(75, 10, 1, 1)
        self.scene.addItem(self.item)

	self.color = QtGui.QColor(0, 0, 0)
        self.color.setNamedColor('#d4d4d4')

	# Crear Timer
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.updateR)
        self.timer.start(200)
        self.i = 0
	self.r = 60

    def updateR(self):
        
        self.i += 1
	self.scene.removeItem(self.item)
	self.item = QtGui.QGraphicsEllipseItem(75, 10, self.r, self.r)
	self.item.setPen(self.color)
	self.item.setBrush(QtGui.QColor(200, 0, 0))
        self.scene.addItem(self.item)
	self.r += 5
        if self.i > 20:
            self.timer.stop()

        


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    view = MyView()
    view.show()
    sys.exit(app.exec_())


