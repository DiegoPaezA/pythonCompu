# -*- coding: utf-8 -*-

import numpy as np
from scipy import stats
from scipy import interpolate
from scipy import signal


def freqDomainHRV(rr_source,fs = 4.0):
        """
        :param rr_source: rr despues de ser interpolado a 1hz - despues de aplicar filtrohrv
        """  
        #inputs        
        # RR
        
        # fs = 4.0 #cubic spline interpolation rate / resample rate (hz)
        
        #Outputs:   output is a structure containg all HRV. One field for each 
        #           PSD method.
        #           Output units include:
        #               aHF,aLF,aVLF (ms^2)
        #               PSD (ms^2/Hz)
        #               F (Hz)
        #               lfhf ratio                
            
        
                
        t = np.arange(1,len(rr_source)+1,1) # time(s)
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

        #calculate LF/HF ratio
        lfhf = aLF/aHF

        aVLF=np.round(aVLF*100)/100; # round
        aLF=np.round(aLF*100)/100;
        aHF=np.round(aHF*100)/100;
        aTotal=np.round(aTotal*100)/100;
        
        return Pxx,Fxx, aVLF, aLF,aHF, lfhf
        