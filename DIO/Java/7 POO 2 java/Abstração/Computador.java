
import java.util.Scanner;

public class Computador {
     
     public static void main(String[] args) {
          Scanner scanner = new Scanner(System.in);
          MSNMessenger msg = new MSNMessenger();
          Facebook fb = new Facebook();
          Telegram tlm = new Telegram();

          String menu ="""
          Qual vai ser a chamada de hj?
          ----------------------------------
          3 pelo telegram 
          2 pelo Facebook 
          1 pelo MSGMessenger
          --------------------------------

                    """;
          System.err.println(menu);
          int num = scanner.nextInt();
          num -= 1;

          while (true) { 
               if (num == 0){
                    msg.enviarMensagem(num);
                    msg.receberMensagem(num);
                    break;
               }
               else if (num == 1){
                    fb.enviarMensagem(num);
                    fb.receberMensagem(num);
                    break;
               }
               else if (num == 2){
               tlm.enviarMensagem(num);
               tlm.receberMensagem(num);
               break;
               }
               else {
                    System.err.println("escolhar invalida");
                    System.out.println(menu);
                    num = scanner.nextInt();
               }
          }
          
          System.err.println("Fim do sistema");
          // vou para por aqui.
          System.err.println("----------------------------------");
          System.err.println("Testando conecções antes de desligar");
          System.err.println("----------------------------------");
          msg.enviarMensagem(0);
          msg.receberMensagem(0);
          System.err.println("----------------------------------");
          fb.enviarMensagem(1);
          fb.receberMensagem(1);
          System.err.println("---------------------------------");
          tlm.enviarMensagem(2);
          tlm.receberMensagem(2);
   
   
     }

     
}
