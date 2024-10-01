# declarando uma string
nome = "Guilhemer arthr de cavalho"

# acessando o primeiro caracter da string
# Em Python, a indexação começa em 0, então [0] retorna o primeiro caractere
print(nome[0]) 

# acessando o decimo terceiro caracter da string
# Lembre-se de que a indexação começa em 0, então [12] retorna o decimo terceiro caractere
print(nome[12]) 

# obtenha todos os caracteres começando com o decimo primeiro
# ao deixar o segundo parâmetro vazio, ele pega todos os caracteres ate o final
print(nome[10:]) 

# isso nao retornara nada, pois o segundo parametro (fim) e menor que o primeiro (inicio)
print(nome[10:10]) 

# isso tambem nao retornara nada
# o terceiro parâmetro aqui é o 'passo' (o número de índices a pular)
# quando o início é 10 e o final é 10 (o mesmo), ir a passos de 12 não retornará nada
print(nome[10:10:12]) 

# acessando o segundo caracter da string
# Em python, a indexação começa com 0, então [1] retorna o segundo caractere
print(nome[1]) 

# a maneira mais simples de inverter uma string no Python
# o "::" é usado para fazer slicing que pula caracteres
# o "-1" diz para ir de trás para frente
print(nome[::-1])