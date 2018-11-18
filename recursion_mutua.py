def par_impar(n):
    if (par(n)):
        print("El numero es par")
    else:
        print("El numero es impar")


def par(n):
    if(n == 0):
        return 1
    else:
        return impar(n-1)

def impar(n):
    if(n == 0):
        return 0
    else:
        return par(n-1)
    
x = int(input("ingrese un numero para determinar si es o no par de forma recursiva mutua:"))
par_impar(x)