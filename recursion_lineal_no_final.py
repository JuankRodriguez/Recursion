def factorial(numero):
    if(numero > 1):
        return (numero*factorial(numero-1))
    else:
        return 1
    
print(factorial(5))    
#a partir de recursion lineal no final se resuelve lo que es n factorial