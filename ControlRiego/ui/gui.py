# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import sys,  glob,  serial
from PyQt5.QtCore import pyqtSlot,  QTime,  QDate
from PyQt5.QtWidgets import QMainWindow

from .Ui_gui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.setWindowTitle('Control de Riego 2017')    
        
        #Time 
        self.timeAlarm = QTime
        self.timeRTC = QTime
        self.dateRTC = QDate

        self.dateTimeRTC.setDate(QDate.currentDate())
        self.dateTimeRTC.setTime(QTime.currentTime())
        self.comboBoxDias.setCurrentIndex(QDate.currentDate().dayOfWeek() -1)
        
        #Disable buttons
        self.disableButtons()
        
        #Vale Control logic
        self.valveOnOff = True
        
             
    @pyqtSlot()
    def on_openPort_clicked(self):
        """
        Open the choosen comboBox port
        """
        puerto = self.listaPuertos.currentText() #comboBox choosen port
        self.ser = serial.Serial(puerto, 9600, timeout=0.1)
        self.ser.close()
        self.ser.open()
        self.enableButtons()
        self.openPort.setEnabled(False)
        self.closePort.setEnabled(True)   
    @pyqtSlot()
    def on_closePort_clicked(self):
        """
        Close the open serial port, and disable the pushbuttons 
        
        """
        self.ser.close()
        self.disableButtons()
        
    @pyqtSlot()
    def on_scanPort_clicked(self):
        
        """
        Fill comboBox with the availables ports
        If there is nothing, the comboBox will show null
        """
        self.puertos = self.serial_ports() #scan serial ports functions
        self.listaPuertos.clear() #clear comboBox
        for i in range (0, len(self.puertos)):
            self.listaPuertos.addItem(self.puertos[i]) #comboBox
            
        if(len(self.puertos)==0):
            self.listaPuertos.addItem("Null") 
            self.openPort.setEnabled(False)
            self.closePort.setEnabled(False)   
        else:    
            self.openPort.setEnabled(True)
            

    def serial_ports(self):
        
        """ Lists serial port names

            :raises EnvironmentError:
                On unsupported or unknown platforms
            :returns:
                A list of the serial ports available on the system
        """
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result
    
    def zeroPad(self,  val):
        """
        Add de zero Pad to the minutes and hours, when both are less than 10
        """
        if (len(val)<2):
            return val.rjust(2,'0')
        else: return val
            
            

    def disableButtons(self):
        
        """
        Disable buttons
        """
        self.sendRTC.setEnabled(False)
        self.readRTC.setEnabled(False)
        self.openPort.setEnabled(False)
        self.closePort.setEnabled(False)
        self.sendAlarm.setEnabled(False)
        self.readAlarm.setEnabled(False)
        self.readHumidity.setEnabled(False)
        self.readTemperature.setEnabled(False)
        self.controlValve.setEnabled(False)
        
    def enableButtons(self):
        """
        Enable buttons
        """
        self.sendRTC.setEnabled(True)
        self.readRTC.setEnabled(True)
        self.sendAlarm.setEnabled(True)
        self.readAlarm.setEnabled(True)
        self.readHumidity.setEnabled(True)
        self.readTemperature.setEnabled(True)
        self.controlValve.setEnabled(True)
        self.openPort.setEnabled(True)
        
    def dayOfWeek(self,  weekday):
        """"
        """
        days = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
        return days[weekday - 1]
    #-----------------------------------------------------------------------------------------------------------
    # Functions for action buttons read, send, control 
    #-----------------------------------------------------------------------------------------------------------    
    @pyqtSlot()
    def on_sendAlarm_clicked(self):
        """
        Send the read it hour to the uc 
        """
        self.timeAlarm = self.tiempoConfig.time()
        min = self.zeroPad(str(self.timeAlarm.minute()))
        hour = self.zeroPad(str(self.timeAlarm.hour())) 
        msnHour = "HA"+ hour + ";" + min+ "$"
        #print msnHour
        self.ser.write(msnHour)
        self.ser.flushInput()
        if (str(self.ser.readline())=="$OK\n"):
            #print "Hora Enviada Correctamente"
            self.rxResult.setText("")
            self.rxResult.setText("Hora Alarma: "+ msnHour + " Enviada Correctamente")
            
    @pyqtSlot()
    def on_sendRTC_clicked(self):
        """
        Send date and hour for the configuration of the rtc module
        """
        self.timeRTC = self.dateTimeRTC.time()
        min = self.zeroPad(str(self.timeRTC .minute()))
        hour = self.zeroPad(str(self.timeRTC .hour())) 
        
        self.dateRTC = self.dateTimeRTC.date()
        day = self.zeroPad(str(self.dateRTC.day())) 
        month = self.zeroPad(str(self.dateRTC.month())) 
        year  = self.dateRTC.year() - 2000
        dayofweek = self.comboBoxDias.currentIndex() + 1 
        
        msnDate = "DR" + str(day) + "/" + str(month)+"/"+str(year) + "/" + str(dayofweek)+ "$"
        msnHour = "HR"+ hour + ";" + min+ "$"
        #print msnDate
        #print msnHour
        
        self.ser.write(msnDate)
        self.ser.flushInput()
        if (str(self.ser.readline())=="$OK\n"):
            #print "Data RTC Enviada Correctamente"
            self.rxResult.setText("Date RTC: "+ msnDate + " Enviada Correctamente")
        
        self.ser.write(msnHour)
        self.ser.flushInput()
        if (str(self.ser.readline())=="$OK\n"):
            #print "Hora Enviada Correctamente"
            self.rxResult.setText( self.rxResult.text() + "\nHora RTC: "+ msnHour + " Enviada Correctamente")
        
    @pyqtSlot()
    def on_readRTC_clicked(self):
        """
        Read the actual date and hour of the rtc module
        """
        self.ser.write("RR$")
        self.ser.flushInput()
        hourRTC =  self.ser.readline()
        dateRTC =  self.ser.readline()
        
        dateSplit=  dateRTC.split("/")
        weekday = self.dayOfWeek(int(dateSplit[len(dateSplit)-1]))
        date = dateSplit[0] + "/" + dateSplit[1]+ "/" + str(int(dateSplit[2])+2000)  

        if (str(self.ser.readline())=="$OK\n"):
            #print "Lectura Realizada Correctamente"
            self.rxResult.setText("Hora Actual RTC [24H]: " + hourRTC )
            self.rxResult.setText(self.rxResult.text()  + "Fecha Actual RTC: "+ weekday +", " + date  )
    
    @pyqtSlot()
    def on_readAlarm_clicked(self):
        """
        Slot documentation goes here.
        """
        self.ser.write("RA$")
        self.ser.flushInput()
        hourAlarm=  self.ser.readline()
        if (str(self.ser.readline())=="$OK\n"):
            #print "Lectura Realizada Correctamente"
            self.rxResult.setText("Alarma Configurada a las: " + hourAlarm)
    
    @pyqtSlot()
    def on_readTemperature_clicked(self):
        """
        Slot documentation goes here.
        """
        self.ser.write("RT$")
        self.ser.flushInput()
        if (str(self.ser.readline())=="$OK\n"):
            #print "Lectura Realizada Correctamente"
            self.rxResult.setText("Temperature info")
    
    @pyqtSlot()
    def on_readHumidity_clicked(self):
        """
        Slot documentation goes here.
        """
        self.ser.write("RH$")
        self.ser.flushInput()
        if (str(self.ser.readline())=="$OK\n"):
            #print "Lectura Realizada Correctamente"
            self.rxResult.setText("Humidity info")
    
    @pyqtSlot()
    def on_controlValve_clicked(self):
        """
        Slot documentation goes here.
        """
        
        if(self.valveOnOff == True):
            self.ser.write("CV1$")
            self.valveOnOff = not self.controlValve
            indicador = "Activada"
            self.controlValve.setText("Valve Off")
        elif(self.valveOnOff == False):
            self.ser.write("CV0$")
            self.valveOnOff = not self.valveOnOff
            self.controlValve.setText("Valve On")
            indicador = "Desactivada"
        
        self.ser.flushInput()
        if (str(self.ser.readline())=="$OK\n"):
            #print "Lectura Realizada Correctamente"
            self.rxResult.setText("Control Valvula : " + indicador)
    

