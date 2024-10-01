# importação do modulo random 
import random

# funções do prof:
# 1 gerador de cpf
def gerar_cpf():
    return "".join([str(random.randint(0, 9)) for _ in range(9)])

# 2 gerador dos subconjuntos
def gerar_subconjunto(conjunto):
    return set(random.sample(list(conjunto), int(random.random() * 100)))

""" confirmação de dos 2 tipos de objetos """
conjunto = set()
conjunto2 = {

}
# print(type(conjunto))
# print(type(conjunto2)) 

# resolvendo problema de aparecer 2 cpf iguais 
cpf = 0
for i in range(0,100):
    cpf2 = cpf
    cpf = gerar_cpf()
    while cpf == cpf2:
            cpf = gerar_cpf()
    conjunto.add(cpf)

# CRIAÇãO DOS SUB conjuntos e aplicação dos calculos 
sub_conjunto = gerar_subconjunto(conjunto)
# print(sub_conjunto)
volei_praia = gerar_subconjunto(conjunto)
ginastica = gerar_subconjunto(conjunto)
judo = gerar_subconjunto(conjunto)
sufe = gerar_subconjunto(conjunto)
dois_esportes = judo | sufe
# print(dois_esportes)
# print(judo)
# print(sufe)
todos_esportes = judo & sufe & ginastica & volei_praia
# print(todos_esportes)
# print(sufe)
nenhum_esporte = conjunto - (judo | sufe | ginastica | volei_praia)
# print(nenhum_esporte)

# Criação do dicionario com os cpfs
dados = {
     "judo": judo , 
     "sufe": sufe ,
     'Pelo menos dois esportes': dois_esportes,
     "Todos os esportes": todos_esportes,
     "Nenhum esporte": nenhum_esporte    
}

print(dados)

# porcentagem da quantidade de cpf em cada esporte
print(" =========================================================================")
print("porcentagem no judo: " , len(judo)/ 100 * len(conjunto))
print("porcentagem no surfer: " , len(sufe)/ 100 * len(conjunto ))
print("porcentagem no surfer ou judo: " , len(dois_esportes)/ 100 * len(conjunto))
print("porcentagem em todos outros esportes: " , len(todos_esportes)/ 100 * len(conjunto))
print("porcentagem em nenhum esportes: " , len(nenhum_esporte)/ 100 * len(conjunto))

# porcentagem da quantidade total de cpf "" criei so para confirmar a quantidade de cpf que estão sendo usados do conjunto ""
print(" =========================================================================")
# sobras = conjunto - (judo | sufe | ginastica | volei_praia) 
# print(len(conjunto)/100)
# print(len(sobras)/100 * len(conjunto))
# print(len(conjunto) - len(sobras))



