def comparacao(j,m):
     pontuacao_J = 0
     pontuacao_M = 0
     for i in range(0,3):
          r = int(j[i][0]) * int(j[i][1])
          r2 = int(m[i][0]) * int(m[i][1])
          pontuacao_J += r
          pontuacao_M += r2
     return pontuacao_J , pontuacao_M
     
def crir_list():
     joao = [0]*3
     maria = [0]*3
     for i in range(0,3):
          joao[i] = list(input().split())
     for i in range(0,3):
          maria[i] = list(input().split())
     r = comparacao(joao,maria)
     if r[0] < r[1]:
          return 'MARIA'
     return "JOAO"
                   
teste = int(input())
for i in range(0,teste):
     print(crir_list())

