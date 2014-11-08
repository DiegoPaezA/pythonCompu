'''
Created on 21/04/2014

@author: diegopaez
Codigo utilizado para probar el contador dentro de una funcion externa
'''
#!/usr/bin/python
import time 
import numpy as np

temp = 0; 
num_par= False;  
count = 0;      
n=0
start_time = time.time() # tiempo inicial
a=np.zeros(50) 




def diego ():
    global n;
    global start_time, elapsed_time, end_time;
    print ("------------------------")
    print("Numero Par: ", n)
    print ("------------------------")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Elapsed Time: ", elapsed_time)
    start_time=end_time
    a[n] = elapsed_time 
    n += 1

    if(n==50):
        print a
    
    return 


def par(x):
    temp = x%2
    if(temp==0):
        num_par = True
    else: 
        num_par= False
    return num_par
       
while(count < 100):
    print("Cuenta total", count)
    count = count + 1
    num_par = par(count) 
    time.sleep(.1)
    if(num_par==True):
        diego()

