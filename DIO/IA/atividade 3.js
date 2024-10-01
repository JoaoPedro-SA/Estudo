//Desafios JavaScript na DIO têm funções "gets" e "print" acessíveis globalmente:
//- "gets" : lê UMA linha com dado(s) de entrada (inputs) do usuário;
//- "print": imprime um texto de saída (output), pulando linha.


function microsoftCopilot(funcionalidade) {
     if (funcionalidade === "Gerar conversas") {
         return "Aperfeiçoa respostas do Copiloto com links internos.";
     } else if (funcionalidade === "Transforme conversa em ação") {
         return "Integra Power Platform, Power Automate e prompts de IA.";
     } else if (funcionalidade === "Da vida aos seus sistemas") {
         return "Seleciona conectores de dados para eficiência operacional.";
     } else if (funcionalidade === "Trazer seus próprios modelos do Azure") {
         return "Configura, treina e conecta serviços no Azure, como o Azure OpenAI.";
     }
 }
 
 // Entrada do usuário
 let entrada = gets().trim();
 
 // Chamada da função com a entrada do usuário
 let resultado = microsoftCopilot(entrada);
 
 // Exibindo o resultado, se houver
 print(resultado);