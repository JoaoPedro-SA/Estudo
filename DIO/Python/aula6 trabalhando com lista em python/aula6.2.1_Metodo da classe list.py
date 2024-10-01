## [].remove - tem mesmo funcionalidade do pop, só que seu foco e 
## e eliminar elementos usando a string não o indice
print(" ##### [].remove #####")
linguagens = ["Python","js","TS","Ruyb","PHP","C","C#",'C++'] 

linguagens.remove("C")
linguagens.remove("C#")
linguagens.remove("PHP")

print(linguagens) 

## [].reverse - inverte a lista deixa ao contrario
print('')
print(" ##### [].reverse #####")
linguagens.reverse()
print(linguagens)

## [].sort - usado para determinar a forma de organização da lista
print('')
print(" ##### [].sort #####")
## organizar e forma de ordem alfabética
linguagens2 = ["Python","js","TS","Ruyb","PHP","C","C#",'C++'] 
linguagens2.sort()
#['C', 'C#', 'C++', 'PHP', 'Python', 'Ruyb', 'TS', 'js']
print(linguagens2)

## organizar e formato reverso
print("")
linguagens2.sort(reverse=True)
# ['js', 'TS', 'Ruyb', 'Python', 'PHP', 'C++', 'C#', 'C']
print(linguagens2)

## organizar em formato em tamanho da palavra
print('')
linguagens2.sort(key=lambda x: len(x))
#['C', 'js', 'TS', 'C#', 'PHP', 'C++', 'Ruyb', 'Python']
print(linguagens2)


## organizar em formato em tamanho da palavra só que modo reversor
print('')
linguagens2.sort(key=lambda x: len(x), reverse=True)
# ['Python', 'Ruyb', 'PHP', 'C++', 'js', 'TS', 'C#', 'C']
print(linguagens2)

## função -> len - usado para saber o tamanho de uma lista
print('')
print(" ##### len #####")
linguagens3 = ["Python","js","TS","Ruyb","PHP","C","C#",'C++'] 
print(len(linguagens3)) #8
 
 ## função sorted - faz a mesma coisa do sorted so que e um a função
 ## alem de ser um metodo 
print('')
print(" ##### sorted #####")
linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))  
# ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  
# ["python", "csharp", "java", "js", "c"]