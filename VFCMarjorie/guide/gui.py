# -*- coding: utf-8 -*-

"""
Module implementing TabWidget.
"""

from PyQt4.QtGui import QTabWidget
from .Ui_gui import Ui_TabWidget
from PyQt4 import QtGui, QtCore


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
        
        self.scene=QtGui.QGraphicsScene(self)
        self.graphicsView.setScene(self.scene) #asignar scene al qgraphview
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
                #self.show()
