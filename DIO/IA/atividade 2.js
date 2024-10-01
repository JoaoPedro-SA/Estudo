//Desafios JavaScript na DIO têm funções "gets" e "print" acessíveis globalmente:
//- "gets" : lê UMA linha com dado(s) de entrada (inputs) do usuário;
//- "print": imprime um texto de saída (output), pulando linha.

function githubCopilot(funcionalidade) {
     if (funcionalidade === "GitHub Copilot Chat") {
         return "Interface de chat para devs integrada com VS Code e Visual Studio.";
     } else if (funcionalidade === "GitHub Copilot para solicitações de pull") {
         return "Adiciona tags automáticas de IA em PRs para revisões.";
     } else if (funcionalidade === "GitHub Copilot for Docs") {
         return "Respostas geradas por IA sobre documentação.";
     } else if (funcionalidade === "Copilot para a CLI") {
         return "Compõe comandos e gera sinalizadores para devs, ajudando na sintaxe.";
     }
      else{
          return "Recurso não reconhecido.";
      }
 }
 
 // Entrada do usuário
 let entrada = gets().trim();
 
 // Chamada da função com a entrada do usuário
 let resultado = githubCopilot(entrada);
 
 // Exibindo o resultado, se houver
 print(resultado);