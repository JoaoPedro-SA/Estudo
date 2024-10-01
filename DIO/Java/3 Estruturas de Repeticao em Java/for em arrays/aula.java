public class aula {

     public static void main(String[] args) throws Exception {
     
     int intrusos = 0 ;
     int alunosV = 0;

     String alunos [] = {"JOAO","PEDRO","SIlVA","LUIZ","GABI","LUIZA","RAFAEL"};
     
     for (int i = 0; i < alunos.length; i++){
       if (alunos[i] == "LUIZA" || alunos[i] == "RAFAEL" || alunos[i] == "PEDRO" ){
          intrusos += 1;
          System.out.println(alunos[i] + "E um intruso");
       }
       else{
          alunosV += 1;
          System.out.println(alunos[i] + "E um aluno valido");

       }
        
     }
     System.out.println("\n quantidade de alunos validos: " + alunosV + "\n quantidade de alunos intrusos: " + intrusos);

     }


}
