#/////////////////////////////////
#Recurcion vs Iteracion
#Funcion recursiva 

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        s = (fibonacci(n-1) + fibonacci(n-2))
        return s
    
numero = int(input("Número de la pocicion que desea ver: "))
#la posicion empieza desde el 1. Es decir, no toma el 0 
print(fibonacci(numero))

#/////////////////////////////////
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

# print(suc)
print(*suc, sep = ', ')
