lista = []
## metodo [].append para adicionar algo na lista
print('##### [].append #####')
lista.append(1)
lista.append("Python")
lista.append([40,30,20])

print(lista) #[1 , "Python",[40,30,20] ]

print('')

# metodo [].clear - usado para limpar lista
print('##### [].clear #####')
print(lista) #[1 , "Python",[40,30,20] ]
lista.clear()
print("vazio - >", lista) #[]


## metodo [].copy - usado para fazer uma copia de uma lista
print('')
print('##### [].copy #####')
lista = [1 , "Python",[40,30,20] ]

lista_copia = lista.copy()

print(" esse e a copia -> " , lista_copia)

## metodo [].count e le mostra a posição numerica dos elementos da lista
print('')
print('##### [].count #####')
cores =["vermelho", "azul","verde","azul"]
print(cores.count("vermelho")) #1
print(cores.count("azul")) #2
print(cores.count("verde")) #1
# caso o valor não seja digitado corretamente enttão 
# o valor vai retonar com 0 
print(cores.count("verde4252")) #1

## metodo [].extend - usado para adicionar elementos na lista
print('')
print('##### [].extend #####')

linguagens = ["Python","js","C","C#",'C++']
print(linguagens) # "Python","js","C","C#",'C++'
linguagens.extend(["java","csharp"])
print(linguagens) #"Python","js","C","C#",'C++',"java","csharp"

## metodo [].index - server para indentificar a primeira surgencia do elemento da lista
print('')
print('##### [].index #####')
print(linguagens.index("java")) # 3
print(linguagens.index("Python")) #0

## metodo [].pop - usado para eliminar um unico elemento da lista
print('')
print('##### [].pop #####')
linguagens2 = ["Python","js","TS","Ruyb","PHP","C","C#",'C++'] 
#quando ele ta vazio ele elimina os elementos de traz para frente de 1 em 1
print(linguagens2.pop()) # C++
print(linguagens2.pop()) # C#
print(linguagens2.pop()) # C
print(linguagens2.pop(0)) # Python
print('')
print(linguagens2)
