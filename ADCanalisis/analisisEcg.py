# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 15:10:08 2015

@author: ieb-ufsc
"""

import numpy as np
import pyqtgraph as pg
import matplotlib.pyplot as plt
ecg = np.loadtxt('/home/ieb-ufsc/Escritorio/ADCi2c/ecg30seg.txt')
plt.plot(ecg)
