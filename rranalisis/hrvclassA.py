# -*- coding: utf-8 -*-
# Clase analisis de tiempo de hrv
import numpy as np
from scipy import stats
from scipy import interpolate
from scipy import signal

class hrvclass:
    
    def __init__(self,dadosrr):
        """
        :param dadosrr: Lista con los datos capturados del vector RR
        """ 
        self.dadosrr=dadosrr # Dados originales
        self.dados = self.filtrohrv(self.dadosrr) # datos filtrados, sin artefacto
        self.n = len(self.dados)# numero de puntos
    def filtrohrv(self,rr_source):
        """
        :param rr_source: Elimina artefactos cuando la variacion es mayor a 100ms
        """ 
        rrlen = rr_source.size
        x_old = np.arange(1, rrlen+1)
        x_new = np.arange(1,rrlen,0.125)
        tck = interpolate.splrep(x_old, rr_source, s=0)
        rr_new = interpolate.splev(x_new, tck, der=0)
        rr_end = signal.resample(rr_new,(len(rr_new)/8))
        
        mm = stats.trim_mean(rr_end, 0.1) # Trim 10% at both ends
        iqr = np.subtract(*np.percentile(rr_end, [75, 25]))
        
        hlimit = mm + 1.5*iqr
        llimit = mm - 1.5*iqr
        
        newrr_source=[]
        
        for i in range(0,rrlen):
            
            if rr_source[i] < (hlimit) and rr_source[i] > (llimit):                
                newrr_source.append(rr_source[i])
                
        return newrr_source  
    
    def mediahrv(self):
        
        """
        :param mediahrv: 
        """ 
        self.media=int((1/float(self.n))*np.sum(self.dados))
        return self.media

    def Bpm(self):
        
        """
        :param Bpm: 
        """ 
        
        Bpm = int(60.0/(float(self.media)/(1000.0))) 
        
        return Bpm


    def SDNN(self):
        
        """
        :param SDNN: 
        """ 
        p=[]
        for i in range(0,self.n):
            p.append((self.dados[i] - self.media)**2)
        SDNN = int(np.sqrt(1/(float(self.n) -1)*(np.sum(p))))    
        return SDNN
        
    def RMSSD(self):
        
        """
        :param RMSSD: 
        """ 
        p=[]
        for i in range(1,(self.n - 1)):
            p.append((self.dados[i] - self.dados[i-1])**2)   
        RMSSD = int(np.sqrt(1/(float(self.n) -1)*(np.sum(p))))
        
        return RMSSD 
        
    def NN50(self):
        """
        :param NN50: 
        """ 
        p=0
        for i in range(1,(self.n - 1)):
            if (abs(self.dados[i] - self.dados[i-1]) > 50):
                p += 1
        self.NN50 = p
        
        return self.NN50

    def pNN50(self):
        """
        :param pNN50: 
        """ 
        pNN50 = int(((self.NN50)/(float(self.n)-1)) * 100)
        
        return pNN50

