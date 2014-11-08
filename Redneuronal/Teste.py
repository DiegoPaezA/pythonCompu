__author__ = 'diegopaez'

import numpy as np

from sigmoide import Sigmoide


s=Sigmoide()
w1 = np.loadtxt('w1.txt')
w2 = np.loadtxt('w2.txt')

padron = np.loadtxt('matrixPadronesIn.txt')

padronTest = np.insert(padron[:,0],0,1) # # inserta un limear (1) en la posicion 0

h = s.calcularS(np.dot(w1 , padronTest))

h = np.insert(h,0,1) # inserta un limear (1) en la posicion 0

y = s.calcularS(np.dot(w2 , h))
y = np.around(y,2)

print y



