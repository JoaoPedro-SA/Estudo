public class aula2 {
     
public static void main(String[] args) {
         
     String meunome = "joao pedro";
     System.err.println(meunome);
     int anofabricacao = 2022;
     System.err.println(anofabricacao);
     boolean verdadeira = true;
     System.err.println(verdadeira);
     
     String primeironome = "joao pedro";
     String segundonome = "silva antunes";

     String nomeCompleto = nomeCompleto(primeironome,segundonome);
     System.err.println(nomeCompleto);
     int conta = soma(20,45);
     System.out.println(conta);
     String conta2 = divisao(75, 3);
     System.err.println(conta2);
     }

public static String nomeCompleto(String primeironome, String segundonNome){
     return "Resultado do metodo " + primeironome.concat(" ").concat(segundonNome);
          
     }
         
public static int soma(int num1 , int num2){
     int num = num1 + num2;
     return num;

}

public static String divisao (double num1 , double num2) {
     double num = num1 / num2;  
     String texto = "Resultado da divisão "+ num;
     return texto;
}
}
