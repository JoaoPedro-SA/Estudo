
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

          if (((a + b + c)/3) > 6) {
          System.out.println("Aprovado");
         }
          else if (((a + b + c)/3) == 6) {
          System.out.println("DP");
          }
          else {
          System.out.println("Reprovado");
          }
          scanner.close();

     }
}
