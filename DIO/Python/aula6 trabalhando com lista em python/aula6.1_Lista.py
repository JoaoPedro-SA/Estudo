numeros = [ 1,30 ,21 ,2 ,9 ,65,34]
pares = []

for numero in numeros:
     if numero % 2 == 0: 
          pares.append(numero)
          
print(pares)
print("")
## outra forma que e o metodo cope_Ranger
##                        👇
impares = [numero for numero in numeros if numero % 3 == 0 ]

print(impares)


