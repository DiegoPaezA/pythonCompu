# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 15:58:46 2015

@author: Diego Ricardo Páez Ardila
"""

from hrvclassA import hrvclass
import numpy as np
import pyqtgraph as pg


#rr = np.loadtxt('/home/ieb-ufsc/Escritorio/Disertacion/RegistroECg/Captura27nov-origem/sesion1/rrtomastest1.txt')
#rr = np.loadtxt('/home/ieb-ufsc/Escritorio/Disertacion/RegistroECg/RegistroDiegoplaymario22nov-origem/rrdiegosMario.txt')
#rr = np.loadtxt('/home/ieb-ufsc/Escritorio/Disertacion/RegistroECg/beaglehrv-nexus/rrhiago9dez4.txt')
#pg.plot(rr,pen=(255,0,0), symbolBrush=(255,255,255), symbolPen='w', symbolSize = 4)

rr = np.loadtxt('/home/ieb-ufsc/Escritorio/Disertacion/RegistroECg/diego15testtriger/rrdiego2.txt')

hrvAnalisis = hrvclass(rr) # inicializa la clase
rr_new = hrvAnalisis.filtrohrv(rr) # filter and resample the signal

# analisis de tiempo
print "Media HRV:", hrvAnalisis.mediahrv(), "ms"
print "Bpm: ", hrvAnalisis.Bpm()
print "SDNN: ",  hrvAnalisis.SDNN() , "ms"
print "RMSSD: ", hrvAnalisis.RMSSD(), "ms"
print "NN50: ",  hrvAnalisis.NN50() 
print "pNN50: ", hrvAnalisis.pNN50() , "%"

#analisis en frequencia

Pxx,Fxx,aVLF,aLF,aHF,lfhf  = hrvAnalisis.freqDomainHRV(rr_new,fs = 4.0)

print "VLF:", aVLF, "ms^2"
print "LF:", aLF, "ms^2"
print "HF:", aHF, "ms^2"
print "LF/HF:", "%.4f" % lfhf

#np.savetxt('rrdiegoprocesado.txt', rr_new, fmt = '%i')

#pg.plot(rr_new,pen=(200,200,200), symbolBrush=(255,0,0), symbolPen='w', symbolSize = 4)


win = pg.GraphicsWindow(title="Diego Paez")
win.resize(1000,600)
win.setWindowTitle('HRV - PSD')

p0 = win.addPlot(title = "PSD")
p0.setXRange(0,0.6)
p0.plot(Fxx,Pxx)
p0.setLabel('left', "PSD", units='ms^2/Hz')
p0.setLabel('bottom', "Frequency", units='Hz')
