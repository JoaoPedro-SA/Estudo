public class aula1 {
     
     public static void main (String[] args) throws Exception {
          
          int a = 0;
          int b = 10;

          for (int i = 0; i <= 10; i++) {
               a = i;
               System.out.println(a);
               
          }

          System.out.println("modo decresente");

          for (int i = 10; i >= 0; i = i - 1) {
               b = i;
               System.out.println(b);
               
          }

          System.out.println("\n Outro exemplo\n");

          a = 1;
          b = 20;

          for (int i = 0; i <= b; i++){
               a =  i;
               if (a % 2 == 0){
                    System.out.println(a);
               }              

          }


     }
}    
