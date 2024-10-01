public class Computador {
     
     public static void main(String[] args) {
          MSNMessenger msg = new MSNMessenger();
          MandarArquivo ma = new MandarArquivo();

       //   msg.validarConectadoInternet();
       //   msg.enviarMensagem();
          //msg.salvarHistoricoMensagem();
          //msg.receberMensagem();
          msg.enviarMensagem();
          msg.receberMensagem();
          System.err.println("");
          System.err.println("nova consulta");
          System.err.println("");
          ma.BaixarArquivo();
          ma.ReceberArquivo();
     

     }

     
}
