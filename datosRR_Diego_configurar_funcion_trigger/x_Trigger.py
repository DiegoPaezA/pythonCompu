# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:24:57 2015

@author: ieb-ufsc
"""
import numpy as np
import pyqtgraph as pg

rr = np.loadtxt('/home/diegopaez/PycharmProjects/datosRR_Diego_configurar_funcion_trigger/rrdiego2014-05-15.txt')

vectorTrigerOn = np.loadtxt('/home/diegopaez/PycharmProjects/datosRR_Diego_configurar_funcion_trigger/vectorTiempoOndiego2014-05-15.txt')
vectorTrigerOff = np.loadtxt('/home/diegopaez/PycharmProjects/datosRR_Diego_configurar_funcion_trigger/vectorTiempoOffdiego2014-05-15.txt')

total = 0 
k = 0
trigerOn = []
for i in range(0,len(vectorTrigerOn)):
    while total <= vectorTrigerOn[i]:
        total += rr[k]
        k += 1        
    trigerOn.append(k)
    k = 0 
    total = 0

print "-----------------------", np.sum(rr)
total = 0 
k = 0
trigerOff = []

for i in range(0,len(vectorTrigerOff)-1):
    while total <= vectorTrigerOff[i]:
        total += rr[k]
        k += 1        
    trigerOff.append(k)
    k = 0 
    total = 0
    #raw_input('Press <ENTER> to continue')    
  

win = pg.GraphicsWindow(title="Basic plotting examples")
win.resize(1000,600)
win.setWindowTitle('pyqtgraph example: Plotting')

p0 = win.addPlot(title = "HRV")
p0.plot(rr,pen=(200,200,200), symbolBrush=(255,0,0), symbolPen='w', symbolSize = 4)

for i in range(0,len(vectorTrigerOff)-1):
    lf = pg.LinearRegionItem([trigerOn[i],trigerOff[i]])
    p0.addItem(lf)
    
'''
for i in range(0,len(rr)):
    total += rr[i]
    if total >= vectorTrigerOn[k]:
        print "-------------------------------"
        print total, ">=" , vectorTrigerOn[k]
        print "posicion local: " , i
        print "K Actual : ", k
        raw_input('Press <ENTER> to continue')
        k += 1
'''       
     