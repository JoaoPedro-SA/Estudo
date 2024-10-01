public class MandarArquivo {


     
     public static void BaixarArquivo (){
      
          VerificaVirusNoArquivo();
          System.err.println("Arquivo sendo baixado");
          
     }
     private static void VerificaVirusNoArquivo(){
          System.out.println("arquivo verificado");
          
     }

     public static void ReceberArquivo(){
         
          System.err.println("Arquivo recebido");
     }
}
