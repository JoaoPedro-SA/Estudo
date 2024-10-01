// isso aqui estar tudd errado 
import java.time.LocalDate;

public class ExemploSimples {
     
     public class Pessoa {
          
          public boolean ehMaiorDeIdade(){
               var idade = 18;
               return idade > 18;
          }
     }

          public void PessoaTeste() {
               Pessoa joaozinho = new Pessoa("João", LocalDate.of(2004,1, 1));
               System.out.println(joaozinho.ehMaiorDeIdade());
          }

     }



