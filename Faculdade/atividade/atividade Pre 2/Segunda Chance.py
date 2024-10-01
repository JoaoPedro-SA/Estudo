qtd_alunos = int(input())
i = 0
id = 0
alteraçoes = 0
figurinha = 0
nota_PR = [0.00] * qtd_alunos
nota_PS = [0.00] * qtd_alunos
msg = [''] * qtd_alunos
c = 0
while i < qtd_alunos:
     i += 1
     nota_PR[i-1] = float(input())
i = 0
while i < qtd_alunos:
     i += 1
     nota_PS[i-1] = float(input())
  
          
while qtd_alunos > id:
     id += 1
     if nota_PR[id-1] >= 10:
          figurinha = '-'
          nota_PR1 = nota_PR[id-1]
          msg[id-1] = (f'{figurinha}({id:03}) original: {nota_PR1:05.2f} | final: {nota_PR1:05.2f}')
     else:
          figurinha = '*'
          if nota_PS[id-1] >= 10:
               c += 1
               nota_PR1 = nota_PR[id-1] + 2 
               nota_PR2 = nota_PR[id-1]
               if nota_PR1 >= 10:
                    nota_PR1 = 10
                    msg[id-1] = (f'{figurinha}({id:03}) original: {nota_PR2:05.2f} | final: {nota_PR1:05.2f}')      
               else:
                    msg[id-1] = (f'{figurinha}({id:03}) original: {nota_PR2:05.2f} | final: {nota_PR1:05.2f}')
          else:
               figurinha = '-'
               nota_PR1 = nota_PR[id-1] 
               nota_PR2 = nota_PR[id-1] 
               msg[id-1] = (f'{figurinha}({id:03}) original: {nota_PR2:05.2f} | final: {nota_PR1:05.2f}')

id = 0
print(f"NOTAS ALTERADAS: {c}")
while id < qtd_alunos:
      id += 1
      print(msg[id-1])