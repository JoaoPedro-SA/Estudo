import java.util.Scanner;

public class VerificacaoServico {
    public static void main(String[] args) throws Exception  {
        Scanner scanner = new Scanner(System.in);
        
        // Entrada do serviço a ser verificado
        String servico = scanner.nextLine().trim();
        
        // Entrada do nome do cliente e os serviços contratados
        String entradaCliente = scanner.nextLine().trim();
        
        // Separando o nome do cliente e os serviços contratados
        String[] partes = entradaCliente.split(",");
        String nomeCliente = partes[0];
        boolean contratado = true;
        
        for (int i = 0; i < partes.length; i += 1){
          if (partes[i].equals(servico)){
               System.out.println("Sim"); 
               contratado = false;       
          } 
        }
        if (contratado){
            System.out.println("Nao");
        }
         
       
        // TODO: Verifique se o serviço está na lista de serviços contratados
        
        scanner.close();
    }
}