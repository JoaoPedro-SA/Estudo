# parte 4 - operadores Lógicos 
# and - tudo tem que ser verdadeiro para ser true 
# or - só 1 ten que ser verdadeiro para ser true 
print (50 < 100 and 20 != 20) # false
print (50 < 100 and 20 == 20) # true

print('')

print (50 >= 100 or 20 != 20) # false
print (50 > 100 or 20 == 20) # true

# not - e para simbolizar negação para
print('')

print (not(50 >= 100 or 20 != 20)) # false agora vai ser True  
print (not(50 > 100 or 20 == 20))  # true agora vai ser false 

carro = not(input('Qual a marca do seu carro?'))
print(type(carro), 'tipo = ', carro)
carro = carro or True
print(type(carro), 'tipo = ', carro)

