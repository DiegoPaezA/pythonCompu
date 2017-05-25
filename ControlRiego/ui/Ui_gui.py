# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\DiegoPaez\PycharmProjects\ControlRiego\ui\gui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(775, 732)
        MainWindow.setMaximumSize(QtCore.QSize(775, 732))
        MainWindow.setStyleSheet("background-color: rgb(43, 43, 43);")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.titulo = QtWidgets.QLabel(self.centralWidget)
        self.titulo.setGeometry(QtCore.QRect(0, 20, 781, 51))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(18)
        self.titulo.setFont(font)
        self.titulo.setStyleSheet("background-color: rgb(236, 236, 234);")
        self.titulo.setScaledContents(True)
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo.setObjectName("titulo")
        self.listaPuertos = QtWidgets.QComboBox(self.centralWidget)
        self.listaPuertos.setGeometry(QtCore.QRect(110, 90, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        self.listaPuertos.setFont(font)
        self.listaPuertos.setStyleSheet("background-color: rgb(236, 236, 234);")
        self.listaPuertos.setObjectName("listaPuertos")
        self.listaPuertos.addItem("")
        self.openPort = QtWidgets.QPushButton(self.centralWidget)
        self.openPort.setGeometry(QtCore.QRect(340, 90, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        self.openPort.setFont(font)
        self.openPort.setStyleSheet("background-color: rgb(236, 236, 234);")
        self.openPort.setObjectName("openPort")
        self.closePort = QtWidgets.QPushButton(self.centralWidget)
        self.closePort.setGeometry(QtCore.QRect(550, 90, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        self.closePort.setFont(font)
        self.closePort.setStyleSheet("background-color: rgb(236, 236, 234);")
        self.closePort.setObjectName("closePort")
        self.scanPort = QtWidgets.QPushButton(self.centralWidget)
        self.scanPort.setGeometry(QtCore.QRect(10, 90, 93, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        self.scanPort.setFont(font)
        self.scanPort.setStyleSheet("background-color: rgb(236, 236, 234);")
        self.scanPort.setObjectName("scanPort")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 167, 751, 221))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.gridLayoutWidget.setFont(font)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.line_2 = QtWidgets.QFrame(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.line_2.setFont(font)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 0, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(233, 229, 129);")
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.tiempoConfig = QtWidgets.QTimeEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(11)
        self.tiempoConfig.setFont(font)
        self.tiempoConfig.setStyleSheet("background-color: rgb(236, 236, 234);")
        self.tiempoConfig.setAlignment(QtCore.Qt.AlignCenter)
        self.tiempoConfig.setObjectName("tiempoConfig")
        self.verticalLayout_3.addWidget(self.tiempoConfig)
        self.sendAlarm = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(11)
        self.sendAlarm.setFont(font)
        self.sendAlarm.setStyleSheet("background-color: rgb(236, 236, 234);")
        self.sendAlarm.setObjectName("sendAlarm")
        self.verticalLayout_3.addWidget(self.sendAlarm)
        self.readAlarm = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(11)
        self.readAlarm.setFont(font)
        self.readAlarm.setStyleSheet("background-color: rgb(236, 236, 234);")
        self.readAlarm.setObjectName("readAlarm")
        self.verticalLayout_3.addWidget(self.readAlarm)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 2, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(233, 229, 129);")
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.readTemperature = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(11)
        self.readTemperature.setFont(font)
        self.readTemperature.setStyleSheet("background-color: rgb(236, 236, 234);")
        self.readTemperature.setObjectName("readTemperature")
        self.verticalLayout_4.addWidget(self.readTemperature)
        self.readHumidity = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(11)
        self.readHumidity.setFont(font)
        self.readHumidity.setStyleSheet("background-color: rgb(236, 236, 234);")
        self.readHumidity.setObjectName("readHumidity")
        self.verticalLayout_4.addWidget(self.readHumidity)
        self.controlValve = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(11)
        self.controlValve.setFont(font)
        self.controlValve.setStyleSheet("background-color: rgb(236, 236, 234);")
        self.controlValve.setObjectName("controlValve")
        self.verticalLayout_4.addWidget(self.controlValve)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 4, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(233, 229, 129);")
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.dateTimeRTC = QtWidgets.QDateTimeEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(11)
        self.dateTimeRTC.setFont(font)
        self.dateTimeRTC.setStyleSheet("background-color: rgb(236, 236, 234);")
        self.dateTimeRTC.setObjectName("dateTimeRTC")
        self.verticalLayout_2.addWidget(self.dateTimeRTC)
        self.comboBoxDias = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(11)
        self.comboBoxDias.setFont(font)
        self.comboBoxDias.setStyleSheet("background-color: rgb(236, 236, 234)")
        self.comboBoxDias.setMaxVisibleItems(7)
        self.comboBoxDias.setObjectName("comboBoxDias")
        self.comboBoxDias.addItem("")
        self.comboBoxDias.addItem("")
        self.comboBoxDias.addItem("")
        self.comboBoxDias.addItem("")
        self.comboBoxDias.addItem("")
        self.comboBoxDias.addItem("")
        self.comboBoxDias.addItem("")
        self.verticalLayout_2.addWidget(self.comboBoxDias)
        self.sendRTC = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(11)
        self.sendRTC.setFont(font)
        self.sendRTC.setStyleSheet("background-color: rgb(236, 236, 234);")
        self.sendRTC.setObjectName("sendRTC")
        self.verticalLayout_2.addWidget(self.sendRTC)
        self.readRTC = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(11)
        self.readRTC.setFont(font)
        self.readRTC.setStyleSheet("background-color: rgb(236, 236, 234);")
        self.readRTC.setObjectName("readRTC")
        self.verticalLayout_2.addWidget(self.readRTC)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.line_3.setFont(font)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 0, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(10, 400, 751, 61))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(236, 236, 234);")
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.rxResult = QtWidgets.QLabel(self.centralWidget)
        self.rxResult.setGeometry(QtCore.QRect(10, 464, 751, 251))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        self.rxResult.setFont(font)
        self.rxResult.setStyleSheet("background-color: rgb(233, 229, 129);")
        self.rxResult.setText("")
        self.rxResult.setScaledContents(True)
        self.rxResult.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.rxResult.setWordWrap(True)
        self.rxResult.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.rxResult.setObjectName("rxResult")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.comboBoxDias.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titulo.setText(_translate("MainWindow", "Configuración del Sistema de Riego"))
        self.listaPuertos.setItemText(0, _translate("MainWindow", "Lista de Puertos"))
        self.openPort.setText(_translate("MainWindow", "Abrir Puerto"))
        self.closePort.setText(_translate("MainWindow", "Cerrar Puerto"))
        self.scanPort.setText(_translate("MainWindow", "Scan"))
        self.label.setText(_translate("MainWindow", "Configuración Alarma de Riego"))
        self.tiempoConfig.setDisplayFormat(_translate("MainWindow", "h:mm AP"))
        self.sendAlarm.setText(_translate("MainWindow", "Enviar Hora"))
        self.readAlarm.setText(_translate("MainWindow", "Leer Datos Alarma"))
        self.label_5.setText(_translate("MainWindow", "Lectura Variables Ambientales"))
        self.readTemperature.setText(_translate("MainWindow", "Leer Temperatura"))
        self.readHumidity.setText(_translate("MainWindow", "Leer Humedad "))
        self.controlValve.setText(_translate("MainWindow", "Activar Valvula"))
        self.label_4.setText(_translate("MainWindow", "Configuración RTC"))
        self.comboBoxDias.setItemText(0, _translate("MainWindow", "Lunes"))
        self.comboBoxDias.setItemText(1, _translate("MainWindow", "Martes"))
        self.comboBoxDias.setItemText(2, _translate("MainWindow", "Miercoles"))
        self.comboBoxDias.setItemText(3, _translate("MainWindow", "Jueves"))
        self.comboBoxDias.setItemText(4, _translate("MainWindow", "Viernes"))
        self.comboBoxDias.setItemText(5, _translate("MainWindow", "Sabado"))
        self.comboBoxDias.setItemText(6, _translate("MainWindow", "Domingo"))
        self.sendRTC.setText(_translate("MainWindow", "Enviar Fecha y Hora"))
        self.readRTC.setText(_translate("MainWindow", "Leer Datos RTC"))
        self.label_3.setText(_translate("MainWindow", "Información Recibida"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

