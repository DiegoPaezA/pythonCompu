from PyQt4 import QtGui
from Guide.hometab import TabWidget
 

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = TabWidget()
    ui.show()
    sys.exit(app.exec_())


