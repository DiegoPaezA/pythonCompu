# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 12:07:27 2014

@author: Diego Ricardo Páez Ardila
"""

from hrvclassA import hrvclass
import numpy as np
import pyqtgraph as pg
from scipy import signal


from scipy import stats
from scipy import interpolate


#rr = np.loadtxt('/home/ieb-ufsc/Escritorio/Disertacion/RegistroECg/Captura27nov-origem/sesion1/rrtomastest1.txt')
#rr = np.loadtxt('/home/ieb-ufsc/Escritorio/Disertacion/RegistroECg/RegistroDiegoplaymario22nov-origem/rrdiegosMario.txt')
#rr = np.loadtxt('/home/ieb-ufsc/Escritorio/Disertacion/RegistroECg/beaglehrv-nexus/rrhiago9dez4.txt')
#pg.plot(rr,pen=(255,0,0), symbolBrush=(255,255,255), symbolPen='w', symbolSize = 4)

rr = np.loadtxt('/home/ieb-ufsc/Escritorio/Disertacion/RegistroECg/diego15testtriger/rrdiego2.txt')
hrvAnalisis = hrvclass(rr) # inicializa la clase

print "Media HRV:", hrvAnalisis.mediahrv(), "ms"
print "Bpm: ", hrvAnalisis.Bpm()
print "SDNN: ",  hrvAnalisis.SDNN() , "ms"
print "RMSSD: ", hrvAnalisis.RMSSD(), "ms"
print "NN50: ",  hrvAnalisis.NN50() 
print "pNN50: ", hrvAnalisis.pNN50() , "%"

rr_new = hrvAnalisis.filtrohrv(rr)
np.savetxt('rrdiegoprocesado.txt', rr_new, fmt = '%i')

#pg.plot(rr_new,pen=(200,200,200), symbolBrush=(255,0,0), symbolPen='w', symbolSize = 4)

rr_time = np.arange(1,len(rr_new)+1,1)

Pxx,Fxx,aVLF,aLF,aHF,lfhf  = hrvAnalisis.freqDomainHRV(rr_new,fs = 4.0)




win = pg.GraphicsWindow(title="Diego Paez")
win.resize(1000,600)
win.setWindowTitle('HRV - PSD')

p0 = win.addPlot(title = "PSD")
p0.setXRange(0,0.6)
p0.plot(Fxx,Pxx)

# calcular areas
#LF_lo = 0.04
#LF_hi = 0.15
#HF_lo = 0.15 
#HF_hi = 0.4
#
## find the indexes corresponding to the LF and HF regions
#indl = np.where((Fxx>=LF_lo) & (Fxx<=LF_hi))
#indh = np.where( (Fxx>=HF_lo) & (Fxx<=HF_hi) )
#
#limitlf = list(indl[0])
#lf_lo = limitlf[0]
#lf_hi = limitlf[len(limitlf)-1]
#
#limithf = list(indh[0])
#hf_lo = limithf[0]
#hf_hi = limithf[len(limithf)-1]
#lf = pg.LinearRegionItem([Fxx[lf_lo],Fxx[lf_hi]])
#hf = pg.LinearRegionItem([Fxx[hf_lo],Fxx[hf_hi]])
#p0.addItem(lf)
#p0.addItem(hf)


'''
f = np.fft.fft(rr_new) / len(rr_new)
y = abs(f[1:len(f)/2])
dt = x[-1] - x[0]
xfft = np.linspace(0, (0.5*len(x)/dt), len(y))



LF_lo = 0.04
LF_hi = 0.15
HF_lo = 0.15 
HF_hi = 0.4
LF = 0.095
HF = 0.275
pow=0;
pow_cent=0
peak_A=0
peak_F=0
j=1


# find the indexes corresponding to the LF and HF regions
indl = np.where((xfft>=LF_lo) & (xfft<=LF_hi))
indh = np.where( (xfft>=HF_lo) & (xfft<=HF_hi) )

limitlf = list(indl[0])
lf_lo = limitlf[0]
lf_hi = limitlf[len(limitlf)-1]

limithf = list(indh[0])
hf_lo = limithf[0]
hf_hi = limithf[len(limithf)-1]

win = pg.GraphicsWindow(title="Basic plotting examples")
win.resize(1000,600)
win.setWindowTitle('pyqtgraph example: Plotting')

p0 = win.addPlot(title = "HRV")
p0.plot(rr_new,pen=(200,200,200), symbolBrush=(255,0,0), symbolPen='w', symbolSize = 4)
win.nextRow()
p1 = win.addPlot(title="FFT")
p1.plot(xfft,y)
lf = pg.LinearRegionItem([xfft[lf_lo],xfft[lf_hi]])
hf = pg.LinearRegionItem([xfft[hf_lo],xfft[hf_hi]])
p1.addItem(lf)
p1.addItem(hf)

text = pg.TextItem(html='<div style="text-align: center"><span style="color: #FFF;">LF</span><br><span style="color:', anchor=(-0.3,1.3), border='w', fill=(0, 0, 255, 100))
p1.addItem(text)
text.setPos((xfft[lf_lo]+xfft[lf_hi])/2, 6)


text = pg.TextItem(html='<div style="text-align: center"><span style="color: #FFF;">HF</span><br><span style="color:', anchor=(-0.3,1.3), border='w', fill=(0, 0, 255, 100))
p1.addItem(text)
text.setPos((xfft[hf_lo]+xfft[hf_hi])/2, 6)

xpsd = np.linspace(0,1,len(rr_new))
y = np.array(rr_new)
frq = np.linspace(0.003, 0.,0.4)
gram = sp.signal.lombscargle(xpsd, y,frq)

win.nextRow()
p2 = win.addPlot(title="Lomb")
p2.plot(gram)

'''
