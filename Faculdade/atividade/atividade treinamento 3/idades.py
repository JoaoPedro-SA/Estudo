num = 0
cont = 0
nub = 0
while True :
     if cont == 0:      
          num += nub
          r = float(num) / float(1)  
          nub = int(input())
          cont += 1
     else:
          num += nub
          r = float(num) / float(cont)  
          nub = int(input())
          cont += 1
     if nub < 0:  
          print(f"{r:.2f}")
          break
