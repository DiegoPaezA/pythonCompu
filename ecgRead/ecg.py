# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

ecg =np.loadtxt('/home/diegopaez/Escritorio/ecgADC/ecgRaw_1Khz.txt')
Fs = 1000.0 # 250 Hz
Vt = np.arange(0,(len(ecg))/Fs,1/Fs) # % 0 - 60 segundos, pasos de 1/250hz tasa de muestreo  


Ord = 4.0           # Ordem do filtro
Fc1 = 30.0         #F. corte analagica (FPB), Hz
W1c = Fc1/Fs
#----------------------------------------------------
# Coeficientes dos Filtros Butterworth
b, a = signal.butter(Ord, W1c*2, 'low') #FPB
#----------------------------------------------------
#----------------------------------------------------
ecg_pb = signal.filtfilt(b, a, ecg) # aplicar filtro

plt.plot(Vt,ecg_pb)