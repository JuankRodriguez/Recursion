#////////////////////////////////////////////////
#Primer Ejemplo 
def factorial (n):
    if n == 0 or n == 1:
        resultado = 1
    elif n > 1:
        resultado = n * factorial(n-1)
    return resultado

numero = int(input("Número: "))

print(factorial(numero))

#////////////////////////////////////////////////
#Segundo Ejemplo

import sys
 
sys.setrecursionlimit(5000)
 
def factorial2(n):
    if n == 1:
        return 1
    else:
        return n * factorial2(n-1)
 
print(factorial2(1000))
