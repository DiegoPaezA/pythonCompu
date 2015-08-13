import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Event handler')
        self.show()

    def keyPressEvent(self, e):
        print "Tecla Leida: " + e.text()
        if str(e.text()) == "p" or str(e.text()) == "P":
            print "pause"

        elif e.key() == QtCore.Qt.Key_Escape:
            self.close()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()