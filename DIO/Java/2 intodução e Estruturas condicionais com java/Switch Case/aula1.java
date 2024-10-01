
import java.util.Scanner;

public class aula1 {

    public static void main(String[] args) {
        Scanner Scanner = new Scanner(System.in);
        
        String sigla = Scanner.nextLine();
        String tamanho = "";

          while (true) { 
              
        
        if (sigla.equals("P") || sigla.equals("p") ){
          System.err.println("Pequeno");
          tamanho = "Pequeno";
          break;
        } else if (sigla.equals("M") || sigla.equals("m")){
          System.err.println("Medio");
          tamanho = "Medio";
          break;
        } else if (sigla.equals("G") || sigla.equals("g")){
          System.err.println("Grande");
          tamanho = "Grande";
          break;
        } else {
          System.err.println("Não Identificado");
          sigla = Scanner.nextLine();
        }
         
     }
      
          System.out.println("Sua ropa vai ser entregue no tamanho " + tamanho);
    }
}