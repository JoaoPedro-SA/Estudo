public class aula1 {
     
     public static void main(String[] args){

       
     }

     public void saudacao() {
          System.out.println("Olá, seja bem-vindo!");
}    
     
     

     public int gerarNumeroAleatorio() {
          return (int) (Math.random() * 100);
}


     public int calcularSoma(int a, int b) {
          return a + b;
}
     public void imprimirMensagem(String mensagem) {
          System.out.println(mensagem);
}

     public String gerarMensagem(int numero) {
          return "O número gerado foi: " + numero;
}

     boolean verificarConexao() {
    // Verifica se há conexão com a internet
     return true;
}
}
