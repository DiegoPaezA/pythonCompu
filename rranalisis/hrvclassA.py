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
        
        self.newrr_source=[]
        
        for i in range(0,rrlen):
            
            if rr_source[i] < (hlimit) and rr_source[i] > (llimit):                
                self.newrr_source.append(rr_source[i])
                
        return self.newrr_source  
    
    def mediahrv(self):
        
        """
        :param mediahrv: 
        """ 
        self.media=int((1/float(self.n))*np.sum(self.dados))
        
        return self.media
        
    def tempoTotal(self):
        
        """
        :param tempo total do sinal em segundos : 
        """ 
        self.tempoTotal=int(np.sum(self.dados)/1000)
        
        return self.tempoTotal

    def vectorTempo(self):
        
        """
        :param vector tempo para o grafico : 
        """ 
        step = float(self.tempoTotal)/float(len(self.newrr_source))
        self.vectorTempo= np.arange(1,self.tempoTotal+1,step) # Vector de tiempo

        return self.vectorTempo        

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
        
    def freqDomainHRV(self,rr_source,fs = 4.0):
        """
        :param rr_source: rr despues de ser interpolado a 1hz - despues de aplicar filtrohrv
        :param fs: frecuencia de reamostrado para analisis en frecuencia
        """  
        #inputs        
        # RR
        # fs = 4.0 #cubic spline interpolation rate / resample rate (hz)
        
        #Outputs:   
        #           Output units include:
        #               pHF,pLF,pVLF (%)
        #               PSD (ms^2/Hz)
        #               F (Hz)
        #               lfhf ratio                
                
        t = np.arange(1,len(rr_source)+1,1) # time(s) crea vector de tiempo 1hz
        y = rr_source                       # rr (ms)
        
        #preparar y
        y = signal.detrend(y,type='linear')
        y = y-np.mean(y)
        
        # Calcular Welch FFT
        
        # preparar y
        t2 = np.arange(1,t[len(t)-1],1/fs)
        y = interpolate.interp1d(t,y) # cubic representa spline         
        y = y(t2)
        y = y-np.mean(y)
        
        #PSD esitmation with hanning window, 256 points each segment with 50% overlap.
        Fxx, Pxx = signal.welch(y,fs=4.0, window="hanning", nperseg=256, noverlap=128,nfft = (512*2)-1 , detrend="linear")
        
        # calcular areas bajo la curva
        VLF = np.array([0, 0.04])
        LF = np.array([0.04, 0.15])
        HF = np.array([0.15, 0.4])

        #find the indexes corresponding to the VLF, LF, and HF bands
        iVLF = np.logical_and(Fxx >=VLF[0] , Fxx<=VLF[1])
        iLF = np.logical_and(Fxx>=LF[0] , Fxx<=LF[1])
        iHF = np.logical_and(Fxx>=HF[0] , Fxx<=HF[1])

        #calculate raw areas (power under curve), within the freq bands (ms^2)
        aVLF = np.trapz(Pxx[iVLF],Fxx[iVLF])
        aLF = np.trapz(Pxx[iLF],Fxx[iLF])
        aHF = np.trapz(Pxx[iHF],Fxx[iHF])
        aTotal=aVLF+aLF+aHF;
        
        #calculate areas relative to the total area (%)
        pVLF=(aVLF/aTotal)*100;
        pLF=(aLF/aTotal)*100;
        pHF=(aHF/aTotal)*100;
        pTotal=pVLF+pLF+pHF;
        #calculate LF/HF ratio
        lfhf = aLF/aHF
        
        aVLF=(np.round(aVLF*100)/100); # round
        aLF=(np.round(aLF*100)/100);
        aHF=(np.round(aHF*100)/100);

        pVLF=(np.round(pVLF*10)/10); # round
        pLF=(np.round(pLF*10)/10);
        pHF=(np.round(pHF*10)/10);
        
        Pxx = Pxx/np.sqrt(np.sum(Pxx))
        
        return Pxx, Fxx, pVLF, pLF,pHF, lfhf, pTotal
        
        
        
        


