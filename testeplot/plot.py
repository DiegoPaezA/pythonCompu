__author__ = 'diegopaez'
import matplotlib.pyplot as plt
import math
import numpy as np

#print plt.isinteractive() # modo interactivo apagado si es false
# plt.ioff() # modo interactivo off
# plt.ion() # modo interactivo on
# plt.clf   # limpia el lienzo de la grafica
# plt.plot([1,2,3,4])
# print plt.isinteractive()
# plt.show() # muestra el grafico cuando no esta en modo interactivo

#print plt.ishold()  # muestra si el hold esta activo
# plt.hold() # mantiene en pantalla todas las graficas

# plt.plot(np.random.rand(10))
# plt.figure(2) # muestra una segunda ventana
#plt.plot(np.random.rand(10))
# plt.show()

# plt.figure(3)

#plt.ion()

#n=0
 #   plt.subplot(1,2,1)
 #   plt.plot((1,2,3,4,5))

 #   plt.subplot(1,2,2)
 #   plt.plot((5,4,3,2,1))
 #   plt.hold()

from pylab import *
import time

ion()

#tstart = time.time()               # for profiling
x = arange(0,2*pi,0.01)            # x-array
line, = plot(x,sin(x))
i=0
while 1:
    i+=1
#for i in arange(1,200):
    line.set_ydata(sin(x+i/10.0))  # update the data

    draw()                         # redraw the canvas

#print 'FPS:' , 200/(time.time()-tstart)