class Passaro:
     def voar(self):
          print("Voando...")

class Pardal(Passaro):
     def voar(self):
          return super().voar()
     
class Avestruz(Passaro):
     def voar(self):
          print('Avestruz não pode voar')
          
class pinguim(Passaro):
     def voar(self):
          print('so consegue nada')
          
class Aviao(Passaro):
          print('Avião está decolado...')

def plano_voo(obj):
     obj.voar()

p1 = Pardal()
p2 = Avestruz()
p3 = pinguim()

plano_voo(p1)
plano_voo(p2)
plano_voo(p3)
plano_voo(Aviao())
     