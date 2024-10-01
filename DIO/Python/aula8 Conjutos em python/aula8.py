## set tirar a duplicidade de elementos de uma lista 
print(set([1,2,3,4,1,3])) #{1, 2, 3, 4}
print(set("abacaxi")) # {'a', 'x', 'c', 'b', 'i'}

print(("palio","gol","Celta","palio","Fiat","gol)"))
# ('palio', 'gol', 'Celta', 'palio', 'Fiat', 'gol)')

print({"palio","gol","Celta","palio","Fiat","gol)"})

print('')
print('Converter o set para uma lista')

numeros = {1,2,3,4}

numeros = list(numeros)

numeros[0]


### Metodos com set. 

## {}.union faz a união dos conjutos
print('')
print('##### {"}.union ##### ')

conjunto_a = {1,2}
conjunto_b = {3,4}

print(conjunto_a.union(conjunto_b)) #{1, 2, 3, 4}

## {}.intersection mostra os valores que os conjunto possui 
## iguais 
print('')
print('#####  {#}.intersection ##### ')

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

print(conjunto_a.intersection(conjunto_b)) # {2, 3}

## {}.difference mostra a diferencia do que um conjunto tem do outro

print('')
print('#####  {#}.difference ##### ')

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

print(conjunto_a.difference(conjunto_b)) # {1}
print(conjunto_b.difference(conjunto_a)) # {4}

##{#}.symmetric_difference - mostra todos os elementos que não são indenticos dos 2 conjuntos
print('')
print('#####  {#}.symmetric_difference ##### ')
conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

print(conjunto_a.symmetric_difference(conjunto_b)) # {1, 4}

## {}.issubset - fala ser todos elementos de um conjuto A
## etar dentro de um conjuto B e vise versa
print('')
print('#####  {#}.issubset##### ')
conjunto_a = {1,2,3}
conjunto_b = {4,1,2,5,6,7,3}

print(conjunto_a.issubset(conjunto_b))# True
print(conjunto_b.issubset(conjunto_a))# False

## {}.issuperset e o oposto do issubset - verifica ser os conjuto A
## estão dentro de B

print('')
print('#####  {#}.issuperset #####  ')
conjunto_a = {1,2,3}
conjunto_b = {4,1,2,5,6,7,3}

print(conjunto_a.issuperset(conjunto_b))# False
print(conjunto_b.issuperset(conjunto_a))# True