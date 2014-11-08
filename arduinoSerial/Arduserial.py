__author__ = 'diegopaez'
# Software para testar la comunicacion serial usando arduino y python
#!/usr/bin/env python

import time
import warnings
from collections import deque

import serial

import numpy as np
import matplotlib.pyplot as plt


#N = 400
#data = deque([0] * N, maxlen=N)  # deque con longitud maxima N

#Creamos la figura
#plt.ion()
#fig, ax = plt.subplots()
#ll, = ax.plot(data)
data = []
# Abrimos la conexion con Arduino
arduino = serial.Serial('/dev/tty.usbmodem411', baudrate=115200 , timeout=1.0)


while True:
    try:
        line = arduino.readline()
        xx = np.fromstring(line.decode('ascii', errors='replace'),sep=' ')
       # xx /= 1241 12bits
        xx /= 77.56
        data.extend(xx)
       # ll.set_ydata(data)
       # ax.set_ylim(min(data) - 1, max(data))
       # plt.pause(0.001)
       # datos = np.fromstring(line.decode('ascii', errors='replace'), sep=' ')

        #pint line
    except ValueError:
            warnings.warn("Line {} didn't parse, skipping".format(line))

    except KeyboardInterrupt:
            print("Exiting")


            break
arduino.close()
print data.__len__()
np.savetxt('captura.csv', data ,fmt = '%10.3f')
plt.plot(data)
plt.show()
