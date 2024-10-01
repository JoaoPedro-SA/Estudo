print('for - break')
print('')

numero = 0
for numero in range(100):
  if (numero <= 10):
         print(numero)
  else:
     break

numero = 0

print('')
print('while - break')
print('')
while(numero <= 10):
     numero += 1
     if(numero == 5):
         break 
     print(numero)
     
print('')         
print('while - continue')
print('')


numero = 0
while(numero < 10):
     numero += 1
     if(numero > 3 and numero < 7):
         continue
     print(numero)    

         