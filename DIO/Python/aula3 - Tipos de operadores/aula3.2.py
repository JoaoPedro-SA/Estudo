# parte 5 - Operadores de indentidade 

# Esse operador compara ser a variavel x oucupa o mesmo local da mememoria de uma vairavel Y.

curso = "Cursos de Python"
nome_curso = curso 
print(curso is nome_curso) 
print(curso is not nome_curso)
print('')

saldo,limite = 200, 200
print(saldo is limite)
print(saldo is not limite)

print('')
saldo,limite = 200, "500"
print(saldo is limite)
print(saldo is not limite)

# parte 6 - operadores de associação

# verifica se o valor aparecer em uma lista ou Array 

cursos = "Curso de Python "
frutas = ['laranja', 'uva', 'limão']
saques = [1500 ,100]

'Pyhon' in cursos

'maça' not in frutas

'200' in saques 
