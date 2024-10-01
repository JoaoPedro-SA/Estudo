
import java.util.Scanner;

public class media {
     
     public static void main(String[] args) {
         Scanner scanner = new Scanner(System.in);

         System.err.println("Qual a nota da AP1 ");
         double a = scanner.nextDouble();
         System.err.println("Qual a nota da AP2 ");
         double b = scanner.nextDouble();
         System.err.println("Qual a nota da Final ");
         double c = scanner.nextDouble();

          if (((a + b + c)/3) > 6 && ((a + b + c)/3) != 10) {
          System.out.println("Aprovado");
         }
          else if (((a + b + c)/3) == 6) {
          System.out.println("DP");
          }
          else if (((a + b + c)/3) == 0) {
               System.out.println("Expulsão ");
               }    

          else if (((a + b + c)/3) == 10) {
                    System.out.println("Genio");
               }
          else if (((a + b + c)/3) > 0) {
                    System.out.println("Não pode notas negativas");
               }
          else if (((a + b + c)/3) > 10) {
                    System.out.println("não pode notas acima de 10");
               }
          else {
          System.out.println("Reprovado");
          }
          scanner.close();

     }
}
