inicio_ano = int(input())
fim_ano = int(input())
i = 0
c = 0
while inicio_ano <= fim_ano:
     conta1 = 0 == inicio_ano % 4 and  0 != inicio_ano % 100
     conta2 =  0 == inicio_ano % 400
     if conta1 or conta2:
          print(inicio_ano)
          c += 1
     inicio_ano += 1
print(f'bissextos: {c}')