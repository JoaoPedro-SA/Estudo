num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())
i = 0
x = 0
for i in range(0, 5):
     num = [num1,num2,num3,num4,num5]
     if num[i] % 2 == 0:
          x = x + 1
print(f"{x} valores pares")   
     