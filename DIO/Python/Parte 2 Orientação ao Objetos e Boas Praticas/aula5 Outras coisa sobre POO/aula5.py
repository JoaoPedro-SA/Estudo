class Pessoa:
     def __init__(self,nome,idade):
          self.nome = nome
          self.idade = idade
          
     def criar_apartir_data_nacimento(self, ano,mes,dia,nome):
          idade = 2022 - ano
          return Pessoa(nome,idade)
     
p = Pessoa("Guilherme" , 28)
print(p.nome , p.idade)

