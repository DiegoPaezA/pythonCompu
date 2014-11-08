# coding=utf-8
__author__ = 'diegopaez'

#from Padrones import Padrones
#from Entrenamiento import Entrenamiento

from Training import Training

import matplotlib.pyplot as plt

# import numpy as np


# Setup

A = [0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1]
C = [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1]
L = [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1]
U = [1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1]

SA = [0, 0, 1, 1]
SC = [1, 1, 0, 0]
#SL = [0, 1, 0, 0]
#SU = [1, 0, 0, 0]




rna = Training(10, 0.1, 0.0025)

rna.inicializarMatrixPadrones(4, 2, 16)

rna.setPadronIn(A, 'A1', 0)
rna.setPadronIn(C, 'C1', 1)
rna.setPadronIn(L, 'L1', 2)
rna.setPadronIn(U, 'U1', 3)

rna.setPadronOut(SA, 'SA1', 0)
rna.setPadronOut(SC, 'SC1', 1)
#rna.setPadronOut(SL, 'SL1', 2)
#rna.setPadronOut(SU, 'SU1', 3)

rna.saveMatrixPadrones('PadronesIn', 'PadronesOut')
rna.inicializarPesos()
rna.addLimearMatrixIn()

ePlot = rna.calcularError()

plt.plot(ePlot)
plt.show()
