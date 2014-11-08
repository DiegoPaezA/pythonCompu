__author__ = 'diegopaez'

import numpy as np
from sigmoide import Sigmoide

class Entrenamiento :

    def __init__(self, neuronas_a, tAprendizado_a, eMinimo_a):
        self.neuronas = neuronas_a
        self.tAprendizado = tAprendizado_a
        self.eMinimo = eMinimo_a

    def inicializarPesos(self,entradas,salidas ):
        self.salidas = salidas
        self.entradas =entradas

        self.w1 = (np.random.rand(self.neuronas,self.entradas + 1))
        self.w2 = (np.random.rand(self.salidas,self.neuronas + 1))


    def addLimearIn(self):
        matrixTemp = np.loadtxt('matrixPadronesIn.txt')
        (self.entradas, self.tPadrones) = np.shape(matrixTemp)
        self.matrixLimear = (np.vstack((np.ones((1,self.tPadrones)),matrixTemp)))


    def calcularError(self):

        Error = 1.0
        ePlot = []
        i = 0
        numMuestras = self.salidas * self.tPadrones
        s = Sigmoide()
        padronesOut = (np.loadtxt('matrixPadronesOut.txt'))

        while Error > self.eMinimo:
            i = i+1

            # Passo Forward
            inCapaoculta =s.calcularS(np.dot(self.w1 , self.matrixLimear))


            (entradas, tPadrones) = np.shape(inCapaoculta)

            outCapaoculta = (np.vstack((np.ones((1,tPadrones)),inCapaoculta)))


            outRed = s.calcularS(np.dot(self.w2,outCapaoculta))

            # calcular error
            error = (padronesOut - outRed)

            Error =np.sqrt((np.sum(np.sum(error**2)))/(numMuestras))
            ePlot.append(Error)
            #Error =np.sqrt(np.sum(np.sum(np.power(error,2)))/numMuestras)

            # Passo Backward

            delta2 = np.multiply(np.multiply(outRed , (1 - outRed)) , error)

            del_w2 = np.dot((2 * self.tAprendizado) , np.dot(delta2 , outCapaoculta.conj().T))



            delta1_temp1 = np.multiply(inCapaoculta, (1 - inCapaoculta))

            delta1_temp2 =np.dot(((self.w2[:,1:self.neuronas+1]).conj().T ) , delta2)

            delta1 = np.multiply(delta1_temp1 , delta1_temp2)

            del_w1 = np.dot((2 * self.tAprendizado) , np.dot(delta1 , (self.matrixLimear).conj().T))

            #actualiza pesos
            self.w1 = self.w1 + del_w1
            self.w2 = self.w2 + del_w2

            if i>500:
                print Error
                i=0

            # print 'Loading ...'


        np.savetxt('w1.txt', self.w1 , fmt = '%10.4f')
        np.savetxt('w2.txt', self.w2 , fmt = '%10.4f')


        print 'Entrenamiento Finalizado'
        return ePlot












