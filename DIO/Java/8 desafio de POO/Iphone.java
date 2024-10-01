
import java.util.Scanner;

public class Iphone{

     public static void main(String[] args) {
          Scanner scanner = new Scanner(System.in);
          AparelhoTelefonico alp = new AparelhoTelefonico();
          NavegadorInternet ni = new NavegadorInternet();
          ReprodutorMusical rm = new ReprodutorMusical();

          String menu = """
                    
          [1] Reprodutor Musica
          [2] Aparelho Telefonico
          [3] Navegador na internet

                    """;
          System.err.println(menu);
          int num = scanner.nextByte();

          while (true) {
               if (num == 1){
                    rm.tocar();
                    rm.pausar();
                    rm.selecionarMusica("Rap de Animme");
                    break;
               }
               else if (num == 2){
                    break;
               }
               else if (num == 3){
                    break;
               }
               else{
                    System.err.println("Erro$@$@$ digita novamente");
                    num = scanner.nextByte();
               }


          }
          
         
     }
}