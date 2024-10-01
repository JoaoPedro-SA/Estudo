public class aula1 {

    public static void main(String[] args) throws Exception {
     
     int i = 0;
     while (true) {
          i += 1;
          if (i == 40) {
               break;
          }
          if (i >= 10 && i <= 20 || (i % 2) == 0) {
               continue;
          }
          else {
          System.out.println(i);
          }

          

     }

    }

}
