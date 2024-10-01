
## {}.isdisjoint - verifica se todos os elementos de um conjuto A
## não estão presente num conjunto B

print('')
print('#####  {#}.isdisjoint #####  ')
conjunto_a = {1,2,3,4,5}
conjunto_b = {6,7,8,9}
conjunto_c = {1,0}

print(conjunto_a.isdisjoint(conjunto_b))# True
print(conjunto_a.isdisjoint(conjunto_c))# False

## {}.add - ultilizado para adicionara elementos no sert

print('')
print('#####  {#}.add #####  ')

sorteio = {1,23}
sorteio.add(25) # {1, 25, 23}
print(sorteio)
sorteio.add(45) # {1, 45, 25, 23}

print(sorteio)
sorteio.add(65) # {65, 1, 45, 23, 25}
print(sorteio)

## {}.clear - faz a limpeza dos elementos do set
print('')
print('#####  {#}.clear #####  ')

sorteio = {1,23}
print(sorteio)
sorteio.clear
print(sorteio)