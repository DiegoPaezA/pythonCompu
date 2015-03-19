# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:24:57 2015

@author: ieb-ufsc
"""
import numpy as np
import pyqtgraph as pg

rr = np.loadtxt('/home/ieb-ufsc/PycharmProjects/datosRR_Diego_configurar_funcion_trigger/rrdiego2014-05-15.txt')

vectorTrigerOn = np.loadtxt('/home/ieb-ufsc/PycharmProjects/datosRR_Diego_configurar_funcion_trigger/vectorTiempoOndiego2014-05-15.txt')
vectorTrigerOff = np.loadtxt('/home/ieb-ufsc/PycharmProjects/datosRR_Diego_configurar_funcion_trigger/vectorTiempoOffdiego2014-05-15.txt')

total = 0 
k = 0
for i in range(0,len(rr)):
    total += rr[i]
    if total >= vectorTrigerOn[k]:
        print "-------------------------------"
        print total, ">=" , vectorTrigerOn[k]
        print "posicion local: " , i
        print "K Actual : ", k
        raw_input('Press <ENTER> to continue')
        k += 1
       
     