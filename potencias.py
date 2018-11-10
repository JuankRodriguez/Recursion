def potencia( a, b):
    #Este programa cunta con 2 numeros que son una base y un exponente
    #
    #   a^b = a^(b/2) × a^(b/2)                si n es par.
    #   a^b = a^(b−1)/2 × a^(b−1)/2 × a        si n es impar.
#     Caso Base
    if b <= 0:
        return 1
    
#     b par
    if b % 2 == 0:
        pot = potencia(a, b/2) # recursion
        return pot * pot
    
#     b impar
    else:
        pot = potencia(a, (b-1)/2) # recursion
        return pot * pot * a
    
    

x = int(input("numero base: "))
y = int(input("numero exponente: "))
print(potencia(x, y))