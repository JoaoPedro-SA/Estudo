i = 0
maior_num = 0
lista = []
num1 = 0
rank = 0
while i <= 99:
     num1 = int(input())
     lista.append(num1)
     num = lista[i] 
     if num > maior_num:
          maior_num = num
          rank = i
     i += 1 
print(maior_num)
print(rank+1)

