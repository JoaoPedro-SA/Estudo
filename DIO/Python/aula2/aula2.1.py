## Parte 3 Variaveis e constantes 

age , name = 26 , 'Joao Pedro'

age2 = 25.6
name2 = 'João Pedro'

print(type(name2), type(age2), type(age))

STATES = [ ### <-- isso e uma forma de fazer a variavel ser sinalizada como uma constante, tem que ser tudo por letra maiscula.
     'SP',
     'RJ',
     'MG'
]
print(STATES) ## sempre de nomes com seguinificado mais simples. 

STATES = 'a' ## mais ainda sim a variavel não vira constante 

## Parte 4 - Conversão de tipos 

print (int(age2) , str(age2))

anos3 = str(age2) 

print(anos3)

print('anos3 tem o seu tipo de variavel = ',type(anos3))

## Parte 5 - Funções entrada(input) saida(print()) 

nome = input('quantos qual e seu nome');
idade = int(input('quantos anos voce tem?'))

print (f'Ola {nome} que bom saber que vc ja tem {idade}, Tenha uma boa noite')

print (nome ,end='...\n')
print( nome , idade,sep='#' ,end='...\n')


