class Cachorro:
     def __init__(self , nome , cor , acordado = True):
          print("Inicializado a classe")
          self.nome = nome
          self.cor = cor
          self.acordado = acordado
          
     def __del__(self):
          print("Removendo a instância da classe.")
          
     
     def falar(self):
          print("auau")
          
def criar_cachorro():
     c = Cachorro("zeus","Branco e preto",False)
     print(c.nome)
          
c = Cachorro("chappie" , "amarelo")
c.falar()

print("Ola mundo")
del c
print("Ola mundo")
print("Ola mundo")
print("Ola mundo")

criar_cachorro()