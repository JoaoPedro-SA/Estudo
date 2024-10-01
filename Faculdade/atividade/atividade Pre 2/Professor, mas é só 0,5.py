num1 = float(input())
num2 = float(input())
M = (num1*0.50) + (num2*0.50) 
def chance():
     num2 = 10
     M = (num1*0.50) + (num2*0.50) 
     if M >=6:
          return True
     else:
          return False
if M >= 6:
     print('aprovado')
elif chance():
     print('talvez com a sub')
else:
     print('reprovado')
     