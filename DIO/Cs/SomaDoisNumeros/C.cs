using System;

namespace SomaDoisNumeros
{
    class Program
    {
        static void Main(string[] args)
        {
            // Solicita o primeiro número ao usuário
            Console.Write("Digite o primeiro número: ");
            string input1 = Console.ReadLine();
            int numero1;
            
            // Verifica se o primeiro número é válido
            while (!int.TryParse(input1, out numero1))
            {
                Console.Write("Entrada inválida. Digite um número inteiro: ");
                input1 = Console.ReadLine();
            }
            
            // Solicita o segundo número ao usuário
            Console.Write("Digite o segundo número: ");
            string input2 = Console.ReadLine();
            int numero2;
            
            // Verifica se o segundo número é válido
            while (!int.TryParse(input2, out numero2))
            {
                Console.Write("Entrada inválida. Digite um número inteiro: ");
                input2 = Console.ReadLine();
            }
            
            // Calcula a soma dos dois números
            int soma = numero1 + numero2;
            
            // Exibe o resultado
            Console.WriteLine($"A soma de {numero1} e {numero2} é: {soma}");
        }
    }
}
