# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 14:59:05 2015

@author: ieb-ufsc
"""
import numpy as np
datos1=['0.99,-0.01,-0.00,-0.14,0.99,0.07,-0.00,0.11,1.00,-0.01,-0.01,0.06,1.00,0.00,0.00,0.03,1.00,0.02,-0.03,0.01,0.99,-0.10,-0.04,-0.08,0.92,-0.02,-0.39,0.03,',
        '0.99,-0.01,-0.00,-0.14,0.99,0.07,-0.00,0.01,1.00,-0.01,-0.01,0.06,1.00,0.00,0.00,0.03,1.00,0.02,-0.03,0.01,0.99,-0.10,-0.04,-0.08,0.92,-0.02,-0.39,0.03,',
        '0.99,-0.01,-0.00,-0.14,0.99,0.07,-0.00,0.11,1.00,-0.01,-0.01,0.06,1.00,0.00,0.00,0.03,1.00,0.02,-0.03,0.01,-0.09,0.08,-0.16,0.85,0.92,-0.02,-0.39,0.03,']
        
n = np.size(datos1)
#print n, m
numSensores = 7
numAngulos = 4 # w,x,y,z 
totalAngulos = numAngulos * numSensores # total angulos leidos

posicionZero = np.zeros((numSensores, numAngulos))
splitAngulos = np.zeros(totalAngulos)
       
splitString = (datos1[0].split(",")) #angulos separados por string

for i in range(0,len(splitString)-1):    
    splitAngulos[i]=(float(splitString[i]))

# salvar posición zero
k = 0 # Variable para recorrer splitAngulos
for i in range(0,numSensores):
    for j in range(0, numAngulos):
        posicionZero[i][j] = splitAngulos[k]
        k +=1    