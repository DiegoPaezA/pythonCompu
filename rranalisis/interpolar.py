# -*- coding: utf-8 -*-

import numpy as np
from scipy import interpolate
from scipy import signal
from scipy import stats

import pyqtgraph as pg




def filtrohrv(rr_source):
        """
        :param rr_source: Elimina artefactos cuando la variacion es mayor a 100ms
        """ 
        rrlen = rr_source.size
        x_old = np.arange(1, rrlen+1)
        x_new = np.arange(1,rrlen,0.125)
        tck = interpolate.splrep(x_old, rr, s=0)
        rr_new = interpolate.splev(x_new, tck, der=0)
        rr_end = signal.resample(rr_new,(len(rr_new)/8))
        
        mm = stats.trim_mean(rr_end, 0.1) # Trim 10% at both ends
        iqr = np.subtract(*np.percentile(rr_end, [75, 25]))
        
        hlimit = mm + 1.5*iqr
        llimit = mm - 1.5*iqr
        
        print ''
        print 'trim mean : ',mm
        print 'iqr : ', iqr
        print 'hlimit : ',hlimit
        print 'llimit : ', llimit
        a = 0        
        newrr_source=[]
        for i in range(0,rrlen):
            
            if rr_source[i] < (hlimit) and rr_source[i] > (llimit):
                print "Ajustar: " , i
                
                newrr_source.append(rr_source[i])  
                a+=1
            
                
                
        print a,rrlen        
        return newrr_source  
        
  
        
#rr = loadtxt('rr_new_diego.txt')
#rr = np.loadtxt('/home/ieb-ufsc/Escritorio/Disertacion/RegistroECg/RegistroDiegoplaymario22nov-origem/rrdiegosMario.txt')
rr = np.loadtxt('/home/ieb-ufsc/Escritorio/Disertacion/RegistroECg/Captura27nov-origem/sesion1/rrtomastest1.txt') 

rr_new = filtrohrv(rr)
pg.plot(rr_new,pen=(200,200,200), symbolBrush=(255,0,0), symbolPen='w', symbolSize = 4)

'''
x_old = np.arange(1, rrlen+1)
x_new = np.arange(1,rrlen,0.125)
tck = interpolate.splrep(x_old, rr, s=0)
rr_new = interpolate.splev(x_new, tck, der=0)

rr_end = signal.resample(rr_new,(len(rr_new)/8))

np.savetxt('rr_end.txt', rr_end, fmt = '%i')

# pgram = np.fft.fft(rr_end)


pg.plot(rr_end,pen=(200,200,200))
#pg.plot(rr_new,pen=(200,200,200), symbolBrush=(255,0,0), symbolPen='w', symbolSize = 4)
'''
