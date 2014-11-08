__author__ = 'diegopaez'
import time


off_time = 0  # Tiempo de parada
stop_time = int(raw_input("Tiempo de ejecucion: "))


start_time = time.time()
while off_time <= stop_time:
    off_time = time.time() - start_time



print off_time

print "Fin"