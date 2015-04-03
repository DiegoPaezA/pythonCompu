# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 22:18:40 2015

@author: diegopaez
"""


import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

indices = [[1, 3], [2], [4]]               # <-----
vals = [[1, 2.5], [1.5], [3.5]]            # <-----
labels = ['Group 1', 'Group 2', 'Group 3']

color_space = iter(cm.Paired(np.linspace(0, 1, len(vals))))
for xs, ys, label in zip(indices, vals, labels):
    col = next(color_space)
    plt.bar(xs, ys, width=1, color=col, label=label)

plt.legend(loc='best')
plt.show()