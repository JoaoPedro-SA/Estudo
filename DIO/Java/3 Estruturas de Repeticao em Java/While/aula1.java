public class aula1 {

     public static void main(String[] args) throws Exception {
     
     int x = 0;
     int r = 0;
     for (int i = 1; i<= 10; i++){

          while (x < 10){
               x++;
               r = x * i;
               System.out.println(i +" x " + x + " = " + r );
          }    
          System.out.println("");
          x = 0;
     }
         
     }
     
}
