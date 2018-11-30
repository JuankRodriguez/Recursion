def operar(numero1, numero2):

    if(numero2 == 0):
        return numero1
    
    elif(numero2 < 0):
        return operar(numero1-1, numero2+1) #recursividad
    
    else:
        return operar(numero1+1, numero2-1) #recursividad
 
 
print("10+3=", operar(5, 2))
print("5-2=", operar(6, -2))

# este ejemplo es muy comprensible pero ineficiente ya que la funcion operar 
# se realiza varias veces gastando memoria y tiempo 
