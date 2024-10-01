def e_perfeito(n):
     if n == 1:
          return False
     i = 0
     r = 0
     while r < n:
          i += 1
          r += i
     if r == n:
          return True
     else:
          return False
def main (x):
     i = 0
     while i < x:
          a = int(input())
          if e_perfeito(a):
               print(f"{a} eh perfeito")   
          else:
               print(f"{a} nao eh perfeito")   
          i += 1
num = int(input())
main(num)