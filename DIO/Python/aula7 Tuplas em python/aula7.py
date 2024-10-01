# tuple _ parecido com a lista mais tem a condição de seus valores são imultaveis

frutas = ("laranja", "pera",'uva')
print(frutas[2])
print(frutas[0])
letras = tuple("python")
print(letras)
numeros = tuple([1.2,3,4])
print(numeros)
print(numeros[-1])
pais = ("Brasil",)
print(pais)

## declaração em formato de matriz
matriz = (
     (1 , "a",2),
     ('b', 3, 4),
     (6, 6 ,'c'),
)

print('')
print(matriz [0])
# (1,"a", 2)
print(matriz[0][0])
# 1
print(matriz[0][-1])
# 2
print(matriz[-1][-1])
# "c"