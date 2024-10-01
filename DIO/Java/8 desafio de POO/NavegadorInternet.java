

public class NavegadorInternet {

     public static void exibirPagina(String url){
          adicionarNovaAba();
          atualizarPagina();
          System.err.println("Exibindo pagina htpp//:" + url +".com.br" );
          


     }
     
     private static void adicionarNovaAba(){
          System.out.println("Abrindo uma nova Aba");
     }

     private static void atualizarPagina(){
          System.err.println("atualizando a Pagina");
     }
}
