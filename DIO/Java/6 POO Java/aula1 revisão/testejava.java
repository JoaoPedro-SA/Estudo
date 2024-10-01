import java.util.Scanner;



public class testejava {
     
     public static void main (String[] arg)  {
          Scanner scanner = new Scanner(System.in);
          System.out.println("Ola Mundo");
          System.out.println("");
          System.err.println(soma(22,54));
          System.out.println("");
          int num = scanner.nextInt(); 
          soma_texto(74,82,num);
          System.out.println(eleva_ate_x(5.25,3.98, num));
          while (true) {
          try {
               int num2 = scanner.nextInt(); 
               System.out.println(eleva_ate_x(5.25,3.98, num2 ));
               break;
          } catch (Exception e) {       
               System.err.println("Deu erro Escreva o numero novamente");
               break;
         }

          

     }
          
          System.err.println("FIm do codigo");

          
     }

     public static int soma(int x,int y){
          int c = x + y;
          return c ;

     }

     public static void soma_texto(int x, int y, int num){
          int c = (x + y) / num;
          System.err.println(c);
     }

     public static double eleva_ate_x(double x, double y, int num ){
          double c = 0.0;
          double d = 0.0;
          while (num <= 10) {
               c += x * y / num;
               num += 1;
          }

          for (int i = 0 ; i < 10 ; i += 1 ){
               d += i * x * y;

          }

          return  (c + d) / num ;
     }
     


}
