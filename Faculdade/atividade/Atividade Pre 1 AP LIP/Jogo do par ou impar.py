
## um metodo diferente 

num1 = input('')
num1 = int(num1)



def par (num1):
          resto = num1 % 2 
          if (resto == 2 or resto == 0):
               num2 = num1
               par = num2 + 2
          else:
               par = num1 + 1
          return par      
          
def impar (num1):
          resto = num1 % 2 
          if (resto == 2 or resto == 0):
               num2 = num1
               impar1 = (num2 + 2) - 3
          else:
               impar1 = (num1 + 1) -3
          
          return impar1
valorIMP = impar(num1)
valorPAR = par(num1)

print('')

print(F"{valorIMP}",F"{valorPAR}")


## resposta 

num1 = int(input())

def par(num1):
    if num1 % 2 == 0:
        par = num1 + 2
    else:
        par = num1 + 1
    return par

def impar(num1):
    if num1 % 2 == 0:
        impar1 = (num1 + 2) - 3
    else:
        impar1 = (num1 + 1) - 3
    return impar1

valorIMP = impar(num1)
valorPAR = par(num1)

print(valorIMP, valorPAR)