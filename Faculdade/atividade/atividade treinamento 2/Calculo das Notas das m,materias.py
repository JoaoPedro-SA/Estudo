
pre1 = float(input('Nota da pre 1 (1/0):'))
pre2 = float(input('Nota da pre 2 (1/0)::'))
AP1 = float(input('Nota da AP1 1 :'))
AP2 = float(input('Nota da AP1 2 :'))
main =  float(input('Nota da PR ou PS :'))
soma_pre = (pre1 * 0.5)  + (pre2 * 0.5) 
soma_ap = (AP1 * 0.5) + (AP2 * 0.5) 
Prova = main * 0.5
map = soma_pre + soma_ap
nf = (Prova + map) 

if (nf >= 6):
     print(F'sua nota e {nf}')
     print('Voce foi aprovado na materia')
     print(F'sua nota das Materias Pre + AP e {map} / 5.0')
     print(F'Sua notas das Pre APS somados foi de {soma_pre} / 1.0')
     print(F'Sua notas das APS somados foi de {soma_ap} / 4.0')
     print(F'sua nota da prova foi {Prova} / 5.0')
else:
     print(F'sua nota e {nf}')
     print('Voce foi reprovado na materia')
     print(F'sua nota das Materias Pre + AP e {map} / 5.0')
     print(F'Sua notas das Pre APS somados foi de {soma_pre} / 1.0')
     print(F'Sua notas das APS somados foi de {soma_ap} / 4.0')
     print(F'sua nota da prova foi {Prova} / 5.0')



