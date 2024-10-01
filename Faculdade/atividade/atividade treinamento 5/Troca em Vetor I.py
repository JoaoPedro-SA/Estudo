v = [0] * 20
for i in range(0,20):
     v[i] = int(input())
i = 19
d = 0
while d < 10:
     s = v[i]
     s1 = v[d]
     v[d] = s
     v[i] = s1
     i -= 1
     d += 1
i = 0
while i < 20:
     print(f'N[{i}] = {v[i]}')
     i += 1
     
     
     