__author__ = 'diegopaez'
import numpy as np


class Sigmoide:

    def __init__(self, x=1):
        self.x = x

    def calcularS(self, x1):

        return (1/ (1 + np.exp(-x1))) #logistica


