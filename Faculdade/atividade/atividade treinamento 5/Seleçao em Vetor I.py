v = [0] * 100
for i in range(0,100):
     v[i] = float(input())
     if v[i] <= 10:
          print(f'A[{i}] = {v[i]}')