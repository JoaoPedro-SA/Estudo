//Desafios JavaScript na DIO têm funções "gets" e "print" acessíveis globalmente:
//- "gets" : lê UMA linha com dado(s) de entrada (inputs) do usuário;
//- "print": imprime um texto de saída (output), pulando linha.

function copilot_no_bing(funcionalidade) {
     if (funcionalidade === "Resumo de pesquisas") {
         return "Processa consultas e resumos utilizando resultados da web.";
     } else if (funcionalidade === "Interações por chat") {
         return "Permite conversar via texto, imagem ou entrada de voz.";
     } else if (funcionalidade === "Geração de conteúdo criativo") {
         return "Facilita a criação de poemas, piadas, histórias e imagens digitais.";
     } else {
         return "Recurso não reconhecido.";
     }
 }
 
 // Entrada do usuário usando "gets" na DIO
 let entrada = gets().trim();
 
 // Chamada da função com a entrada do usuário
 let resultado = copilot_no_bing(entrada);
 
 // Exibindo o resultado usando "print" na DIO
 print(resultado);