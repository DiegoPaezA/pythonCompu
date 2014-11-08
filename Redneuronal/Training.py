__author__ = 'diegopaez'
import numpy as np

from sigmoide import Sigmoide


class Training:
    def __init__(self, neuronas_a, taprendizado_a, eminimo_a):
        """
        :param neuronas_a:
        :param tAprendizado_a:
        :param eMinimo_a:
        :return:
        """
        self.neuronas = neuronas_a
        self.tAprendizado = taprendizado_a
        self.eMinimo = eminimo_a

    def inicializarMatrixPadrones(self, numpadronesin, numpadronesout, numpuntospadronin):
        """
        :param numpadronesin:
        :param numpadronesout:
        :param numpuntospadronin:
        """
        self.numpadronesin = numpadronesin
        self.numpadronesout = numpadronesout
        self.numpuntospadronin = numpuntospadronin

        self.MatrixIn = np.ones((numpadronesin, numpuntospadronin))
        self.MatrixOut = np.ones((numpadronesout, numpadronesin))

    def setPadronIn(self, padron, nombre, num):
        """
        :param padron:
        :param nombre:
        :param num:
        :return:
        """
        np.savetxt('Padron' + nombre + '.txt', padron, fmt='%10.2f')
        self.MatrixIn[num, :] = padron

    def setPadronOut(self, padron, nombre, num):
        """
        :param padron:
        :param nombre:
        :param num:
        :return:
        """
        np.savetxt('Padron' + nombre + '.txt', padron, fmt='%10.2f')
        self.MatrixOut[num, :] = padron

    def saveMatrixPadrones(self, nombrein, nombreout):
        """

        :param nombrein:
        :param nombreout:
        :return:
        """
        self.nombrein = nombrein
        self.nombreout = nombreout
        np.savetxt('matrix' + self.nombrein + '.txt', self.MatrixIn.conj().T, fmt='%10.2f')
        np.savetxt('matrix' + self.nombreout + '.txt', self.MatrixOut, fmt='%10.2f')

    def getMatrixPadrones(self, nombre):
        """
        :param nombre:
        :return:
        """
        return np.loadtxt('matrix' + nombre + '.txt')

    def inicializarPesos(self):
        """
        :return:
        """
        self.w1 = (np.random.rand(self.neuronas, self.numpuntospadronin + 1))
        self.w2 = (np.random.rand(self.numpadronesout, self.neuronas + 1))

    def addLimearMatrixIn(self):
        """

        :return:
        """
        matrixTemp = np.loadtxt('matrix' + self.nombrein + '.txt')
        (self.entradas, self.tPadrones) = np.shape(matrixTemp)
        self.matrixLimear = (np.vstack((np.ones((1, self.tPadrones)), matrixTemp)))

    def calcularError(self):
        """

        :return:
        """

        Error = 1.0
        ePlot = []
        i = 0
        numMuestras = self.numpadronesout * self.numpadronesin

        s = Sigmoide()
        padronesOut = (np.loadtxt('matrix' + self.nombreout + '.txt'))

        while Error > self.eMinimo:
            i += 1

            # Passo Forward
            inCapaoculta = s.calcularS(np.dot(self.w1, self.matrixLimear))

            (entradas, tPadrones) = np.shape(inCapaoculta)

            outCapaoculta = (np.vstack((np.ones((1, tPadrones)), inCapaoculta)))

            outRed = s.calcularS(np.dot(self.w2, outCapaoculta))
            # calcular error
            error = (padronesOut - outRed)

            Error = np.sqrt((np.sum(np.sum(error ** 2))) / (numMuestras))
            ePlot.append(Error)

            # Passo Backward

            delta2 = np.multiply(np.multiply(outRed, (1 - outRed)), error)

            del_w2 = np.dot((2 * self.tAprendizado), np.dot(delta2, outCapaoculta.conj().T))

            delta1_temp1 = np.multiply(inCapaoculta, (1 - inCapaoculta))

            delta1_temp2 = np.dot(((self.w2[:, 1:self.neuronas + 1]).conj().T ), delta2)

            delta1 = np.multiply(delta1_temp1, delta1_temp2)

            del_w1 = np.dot((2 * self.tAprendizado), np.dot(delta1, (self.matrixLimear).conj().T))

            # actualiza pesos
            self.w1 = self.w1 + del_w1
            self.w2 = self.w2 + del_w2

            if i > 500:
                print Error
                i = 0

        np.savetxt('w1.txt', self.w1, fmt='%10.4f')
        np.savetxt('w2.txt', self.w2, fmt='%10.4f')

        print 'Entrenamiento Finalizado'
        return ePlot