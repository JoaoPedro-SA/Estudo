numero = int(input('escolha um numero'))
texto =  input('informe um texto')

VOGAIS = "AEIOU"
for letra in texto:
     if letra.upper( ) in VOGAIS:
          print(letra,end="")
else:
     print('')
     print('execulta no final do laço')

# adiciona uma quebra de linha
limite = 10 - numero - 1
for texto in range(limite):
     numero += 1
     print (numero)
     
frutas = [" maçã ", " banana ", " laranja "]

for fruta in frutas:
  print(fruta)


while numero != 101:
     numero = numero + 1
     print(numero-1)
     
     
     