# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 15:10:08 2015

@author: ieb-ufsc
"""

import numpy as np
import pyqtgraph as pg
import matplotlib.pyplot as plt

ecg = np.loadtxt('/home/diegopaez/PycharmProjects/ADCanalisis/ecg30seg.txt')
plt.plot(ecg)
plt.show()

#plt.fill(ecg, facecolor='blue', alpha=0.5)
#fill_between
