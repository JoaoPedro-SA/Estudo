def sacar(saldo): 
     valor = int(input('qual e o valor que vc quer sacar '))
    
     if (saldo >= valor): 
          print('valor sacados!')
          print('restire o seu bilhete na boca do caixa')
     
     else:
          print('esse valor e maior que seu saldo')
     
         
     print('Obrigado por ser nosso cliente tenha um bom dia')
  
saldo_usuario1 = 700        
sacar(saldo_usuario1)