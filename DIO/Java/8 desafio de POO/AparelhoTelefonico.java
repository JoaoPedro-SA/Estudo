public class AparelhoTelefonico {
     
     public static void ligar (String numero){
          System.err.println("Ligando para o numero " + numero);
          atender(numero);
     }    

     private static void atender(String numero){
          System.err.println("Atendendo o numero " + numero);
     }

     public static void iniciarCorreioVoz(){
          System.err.println("iniciando Correio de Voz");
     }

}
