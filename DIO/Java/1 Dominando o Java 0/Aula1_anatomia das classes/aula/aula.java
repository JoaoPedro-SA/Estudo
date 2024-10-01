import java.util.Scanner;
public class aula {

     public static void main (String [] args) {
          System.out.print("Ola Mundo \r\n");
          
          Scanner scanner2 = new Scanner(System.in);
  
          System.out.print("Qual é o seu nome? ");
          String nome = scanner2.nextLine();
  
          System.out.print("Quantos anos você tem? ");
          int idade = scanner2.nextInt();
  
          System.out.println("Olá, " + nome + "! Você tem " + idade + " anos.");
  
          scanner2.close();

     }
   
   
}



 
