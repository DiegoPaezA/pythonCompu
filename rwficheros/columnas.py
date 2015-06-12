# -*- coding: utf-8 -*-
"""
Created on Fri May  1 20:36:51 2015

@author: diegopaez
"""
import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])
np.savetxt("row.txt", (a,b), fmt="%d")