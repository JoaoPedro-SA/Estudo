import java.util.Scanner;

public class aula {
     
     public static void main(String[] args) throws Exception {
        
          while (true) { 
             try {
                    
          Scanner scanner = new Scanner(System.in);

               System.out.println("Digita um numero:  ");
               int numero = scanner.nextInt();

               System.err.println("voce escolheu esse numero, " + numero);
                break;
                 
          } catch (Exception e /* erro */ ) {
               System.err.println("ERRO");

             }
         
             

         }

     }
}
