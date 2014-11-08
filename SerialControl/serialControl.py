# coding=utf-8
# coding=utf-8

__author__ = 'diegopaez'

import time
import serial as sc
import re



# reiniciar el arduino antes de iniciar la conexion
data1 = []
data2 = []
data3 = []
data4 = []

arduino = sc.Serial('/dev/tty.usbmodem411', baudrate=115200, timeout=1.0)

tmp = 1
loopOn = 1
while loopOn == 1:

    line = arduino.readline()
    print line
    if line == "$$\n":
        arduino.write("$")

        tmp = 0

    while tmp == 0:

        user = int(raw_input("Ingrese 1 para o 2 o 3: "))
        if user == 1:
            arduino.flushInput()
            print "$$$$"
            arduino.write("$$$$")
            time.sleep(.1)
            print arduino.readline()
            # data1.append(arduino.readline())

        elif user == 2:
            print "$CAL"
            arduino.flushInput()
            arduino.write("$CAL")
            time.sleep(.1)
            data2.append(arduino.readline())

        elif user == 3:
            print "$PRI"
            arduino.flushInput()
            arduino.write("$PRI")
            #print arduino.readline()
            data3.append(arduino.readline())

        elif user == 4:
            tmp = 1
            loopOn = 0

    time.sleep(.5)

# print data1, "\n", data2, "\n", data3
print data3

'''
for i in range(0,(len(data3)-1)):
    ((re.split(',', data3[i])))
'''

arduino.close()
