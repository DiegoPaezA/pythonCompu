# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 17:37:50 2015

@author: ieb-ufsc
"""


from hrvclassA import hrvclass
import numpy as np
import pyqtgraph as pg

import matplotlib.pyplot as plt


#rr = np.loadtxt('/home/ieb-ufsc/PycharmProjects/rranalisis/Final/rrdiego14-May-14-23:48:12.txt')
rr = np.loadtxt('/home/diegopaez/PycharmProjects/rranalisis/Final/rrdiego214-May-14-23:54:04.txt')

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


#--------------------------------------------VFC
#fig, ax = plt.subplots()
fig, (ax,ax1) = plt.subplots(2,1)
ax.plot(rr_new,color='black', linewidth = 2,marker='o',markersize=6,markerfacecolor=(1, 0, 0, 1))
ax.set_xlabel("bpm")
ax.set_ylabel("time [ms]")
ax.grid(True)
ax1.grid(True)
#--------------------------------------------Freq
#fig, ax1 = plt.subplots()
ax1.plot(Fxx,Pxx,color='black',linewidth = "2")
ax1.set_xlim(0,0.4)
ax1.set_xlabel("Frequency (Hz)")
ax1.set_ylabel("PSD (ms^2/Hz)")
p3 = Rectangle((0, 0), 1, 1, fc=(0.49,1.0,1.0)) #fc = facecolor
p2 = Rectangle((0, 0), 1, 1, fc=(0.69,0.49,1.0))
p1 = Rectangle((0, 0), 1, 1, fc=(0.49,0.49,1.0))
ax1.legend([p1, p2,p3], ["VLF","LF", "HF"])
#
ax1.fill_between(Fxx,Pxx,0,where=Fxx>=0.14, facecolor=(0.49,1.0,1.0), alpha=1)
ax1.fill_between(Fxx,Pxx,0,where=Fxx<=0.15, facecolor=(0.69,0.49,1.0), alpha=1)
ax1.fill_between(Fxx,Pxx,0,where=Fxx<=0.04, facecolor=(0.49,0.49,1.0), alpha=1)
ax1.axvline(x=0.039,linewidth=4, color='r')
ax1.axvline(x=0.1487,linewidth=4, color='r')


