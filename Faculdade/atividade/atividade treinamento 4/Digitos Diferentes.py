''' fazer o teste de cada unidade'''
''' print(f"esse numero {x} apareceu {cont} vezes ")'''
def teste_unitario(x,numero_todo):
     cont = 0
     for i in numero_todo:
          if x == i:
               cont += 1 
     if cont >= 2:
          return True


''' separar os numeros completos em unidades'''
def filtro_letra_por_letra(x):
    num = str(x)
    for i in num:
        if teste_unitario(i, num):  # Passa x como o segundo argumento
            return True
    return False
     
     
     
''' criar e separar cada numero das listas'''
def criar_lista(n1,n2):
     cont = 0
     n1 = int(n1)
     n2 = int(n2)
     while n1 <= n2:
          n1 = str(n1)
          if False == filtro_letra_por_letra(n1):
               cont +=1
          n1 = int(n1)
          n1 +=1
     return(cont)
     
                 
"""corpo principal do codigo"""
def main(num):
     print(criar_lista(num[0],num[1]))

i = 0
while i < 200:
     i +=1
     try:
         num = list(input().split())
         main(num)
     except EOFError:
         break