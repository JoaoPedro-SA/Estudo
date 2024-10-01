v = [0] * 1000
t = int(input())
num = 0
valor = 0
for i in range(0,1000):
     if valor >= t:
          valor = 0     
     v[num] = valor
     print(f"N[{num}] = {v[num]}")
     num += 1
     valor += 1
     
