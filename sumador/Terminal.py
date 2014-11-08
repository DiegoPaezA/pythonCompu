__author__ = 'diegopaez'
import sumador
import time
d = sumador.Sumador(-1.5, 2.2)
c = sumador.Sumador(-3, 2)
print d.sumar
print c.sumar


def sumar(x, y):
    return x + y


l = [1, 2, 3]
l2 = reduce(sumar, l)
print l2

a = True
while a == True:

    try:
        print "Diego"
    except KeyboardInterrupt:
        time.sleep(1)
        print "Finalizar programa"
        time.sleep(1)
        a = False
print "Termino programa"


