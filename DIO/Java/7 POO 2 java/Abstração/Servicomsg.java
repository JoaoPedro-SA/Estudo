public class Servicomsg {
     String nome [] = {"MSG","FACEBOOK","TElEGRAM" };
     
          public void enviarMensagem(int x) {
               System.out.println("Enviando mensagem para => " + nome[x]);
               validarConectadoInternet();
               salvarHistoricoMensagem();
          }
          public  void receberMensagem(int x) {
               System.out.println("Recebendo mensagem pelo => " + nome[x]);
          }
          private  void validarConectadoInternet() {
               System.out.println("Validando se está conectado a internet");
          }
          private  void salvarHistoricoMensagem() {
               System.out.println("Salvando o histórico da mensagem");
          }
     
     
}
