import java.util.Scanner;

public class SwitchCaseExample {
     public static void main(String[] args) {
        java.util.Scanner Scanner = new Scanner(System.in);
         int escolha = Scanner.nextInt();
         
         switch(escolha) {
             case 1:
                 System.out.println("Você escolheu a opção um");
                 break;
             case 2:
                 System.out.println("Você escolheu a opção dois");
                 break;
             case 3:
                 System.out.println("Você escolheu a opção três");
                 break;
             default:
                 System.out.println("Opção inválida");
         }
     }
 }