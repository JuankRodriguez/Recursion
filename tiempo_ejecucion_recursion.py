#Funcion recursiva 
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        s = (fibonacci(n-1) + fibonacci(n-2))
        return s
    
numero = int(input("Número de la pocicion que desea ver: "))


#////////////////////////////tiempo de ejecucion recursion///////////////////////

import time
t0 = time.clock()
print(fibonacci(numero))
print ("%.6f sec" % (time.clock() - t0))