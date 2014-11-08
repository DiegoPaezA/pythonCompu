# coding=utf-8
# coding=utf-8
__author__ = 'diegopaez'


class Sumador:
    def __init__(self,value1=0,value2=0):
        """
        Aqui se ingresa la descripción de la clase

        :param value1: Variable 1
        :param value2: Variable 2
        """
        self.a = value1
        self.b = value2

    @property
    def sumar(self):
        self.c = self.a + self.b
        return (self.c)
