def Hanoi(n, origen=1, auxiliar=2, destino=3):

    if n > 0:
        Hanoi(n-1, origen, destino, auxiliar) 
        print("Se mueve el disco %d de torre %d a la torre %d" % (n, origen, destino)) 
        Hanoi(n-1, auxiliar, origen, destino) 


print("*"*27)
print("*     TORRES DE HANOI     *")
print("*"*27 + "\n")

discos = int(input("Ingrese numero de discos: "))

Hanoi(discos)