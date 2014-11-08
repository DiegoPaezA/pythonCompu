__author__ = 'diegopaez'
import numpy as np


class Padrones:

    def __init__(self):
        """

        :param num_padron:
        """



    def setPadronIn(self, padron, nombre, num):
        np.savetxt('Padron' + nombre + '.txt', padron, fmt='%10.2f')
        self.MatrixIn[num , :] = padron

    def setPadronOut(self, padron, nombre, num):
        np.savetxt('Padron' + nombre + '.txt', padron, fmt='%10.2f')
        self.MatrixOut[num , :] = padron


    def getPadron(self, nombre):
        return np.loadtxt('Padron' + nombre + '.txt')

    def saveMatrix(self):
        np.savetxt('matrixPadronesIn.txt',self.MatrixIn.conj().T , fmt='%10.2f')
        np.savetxt('matrixPadronesOut.txt',self.MatrixOut.conj().T , fmt='%10.2f')


    def getSizeIn(self):
        return np.shape(self.MatrixIn.conj().T)

    def getSizeOut(self):
        return np.shape(self.MatrixOut.T)

    def setNumPadrones(self,numPadronesIn = 1, numPadronesOut=1):

        self.MatrixIn = np.ones((numPadronesIn,16))
        self.MatrixOut = np.ones((numPadronesOut,numPadronesIn))















