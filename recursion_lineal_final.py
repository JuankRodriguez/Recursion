def mcd(a,b):
    if(a == b):
        return a
    elif(a<b):
        return mcd(a, b-a)
    else:
        return mcd(a-b, b)
print(mcd(4454,143052))
print(mcd(3,9))
#elige el maximo comun divisor entre dos numeros. esto a partir de recursion
#en la recursion lineal final el resultado que devuelve es el resultado de eecucion de la ultima llamada recursiva