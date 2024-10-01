# Desafio de bicecletaria.

class bicicleta:
     def __init__(self, cor , modelo, ano , valor):
          self.cor = cor
          self.modelo = modelo
          self.ano = ano
          self.valor = valor
          
     def bulzinar(self):
          print("Plinm plim...m")
          
     def parar(self):
          print("Parando bicicleta...")
          print("Bicicleta parada!")
     
     def correr(self):
          print("Vrummmmmm...")
          
     def getcor(self):
          return self.cor
     
    # def __str__ (self):
     #     return f"Bicicleta: cor={self.cor}, modelo={ self.modelo}, ano={self.ano},valor={self.valor}"
     
     def __str__(self):
          return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

     
     
     
b1 = bicicleta( "vermelha" , "caloi", 2022, 600)
b1.bulzinar()
b1.correr()
b1.parar()
print((b1.modelo,b1.ano,b1.valor))


b2 = bicicleta("verde","monark",2000,189)
bicicleta.bulzinar(b2)
b2.bulzinar()
b2.getcor()
print(b2.cor)
print(b2)