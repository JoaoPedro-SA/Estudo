frutas = ["laranja","maça","uva"]
print(frutas)
print('')

frutas1 = []
print(frutas1)
print('')


letras = list('python')
print(letras)
print('')


numeros = list(range(10))
print(numeros)
print('')


carro = ['ferrari','f8',42000000,2020,2900,"são Paulo",True]
print(carro)
print('')
print(carro[0])##ferrari
print(carro[-2])## São Paulo
print('###### Matrizes #######')

numeros3por3 = [
     [1 , 2 , "3"],
     ['4',"5", 6 ],
     [ 7  , 8 , 9]     
]
print(numeros3por3[0])# [1, 2, '3']
print(numeros3por3 [2][0])# 7
print(numeros3por3 [0][2])# 3
print(numeros3por3 [-1][-1])# 9

### Listas
print('')
print('#######_LISTA_##########')
lista = ["p","y","t","h","o","n"]

print(lista[2:])    #['t', 'h', 'o', 'n']
print(lista[:2])    #['p', 'y']
print(lista[1:3])   #['y', 't']
print(lista[0:3:2]) #['p', 't']
print(lista[::])    #['p', 'y', 't', 'h', 'o', 'n']
print(lista[::-1])  #['n', 'o', 'h', 't', 'y', 'p']

## exemplo de acesso de cada lista
print('')
print('########-acesso com for-#######')
carro3 = ['gol','celta','palio']

for i in carro3:
     print(i)
     print('')
for i, carro in enumerate(carro3): # enumerate e um função para numerar a lista ou array
     print(f'{i}: {carro}')
     