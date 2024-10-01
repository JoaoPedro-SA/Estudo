def e_primo(n):
     i = 1
     c = 0
     while i < n:
          r = n % i
          if ( r == 0):
               c +=1
          i += 1
     if c < 2:
          return True
     else:
          return False
def main (x):
     i = 0
     while i < x:
          a = int(input())
          if e_primo(a):
               print(f"{a} eh primo")   
          else:
               print(f"{a} nao eh primo")   
          i += 1


num = int(input())
main(num)