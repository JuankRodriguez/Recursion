#Funcion Iterativa

n = int(input("Ingrese un numero mayor que 0: "))
#realiza la sucecion mostrando todos los numeros menores hasta el ingresado

while n <= 0:
    n = int(input("El numero debe ser mayor que 0: "))

suc = [0, 1]
x = suc[0] + suc[1]

while x <= n:
    suc.append(x)
    a = len(suc)
    b = suc[a - 1]
    c = suc[a - 2]
    x = b + c


#////////////////////////////tiempo de ejecucion iterativa//////////////////////

import time
t0 = time.clock()
print(*suc, sep = ', ')
print ("%.6f sec" % (time.clock() - t0))