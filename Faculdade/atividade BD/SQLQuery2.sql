-- select * from CLIENTE
-- select * from PEDIDO
-- select * from PEDIDO_ITEM
-- select * from PRODUTO
-- select * from VENDEDOR

-- /* 01 � Selecione os Clientes que residem no estado de S�o Paulo? */

-- select * from CLIENTE
-- where UF = 'SP';

-- /* 02 Encontre os Vendedores que tem sal�rio 
-- que variam entre R$2000 e R$4000, n�o esque�a de ordenar a pesquisa por sal�rio? */

-- select * from VENDEDOR
-- where SALARIO >= 2000 and SALARIO <= 4000;

-- /* 03 � Pesquise os Pedidos para a seguinte rela��o de 
-- Clientes(110, 260 e 720), ordene a pesquisa por: CODIGO_CLIENTE, CODIGO_VENDEDOR E CODIGO_PEDIDO! */

-- SELECT * FROM PEDIDO
-- WHERE CODIGO_CLIENTE = 110 OR 
-- CODIGO_CLIENTE = 260 OR 
-- CODIGO_CLIENTE = 720
-- ORDER BY CODIGO_CLIENTE, CODIGO_VENDEDOR ,CODIGO_PEDIDO;

-- /* 04 � Relacione os Itens dos Pedidos para o seguinte intervalo de CODIGO_PEDIDO:
-- de 120 a 140, N�o esque�a de ordenar a apresenta��o do resultado por: CODIGO_PEDIDO, CODIGO_PRODUTO. */

-- SELECT * FROM PEDIDO_ITEM
-- WHERE CODIGO_PEDIDO >= 120 AND 
-- CODIGO_PEDIDO <= 140
-- ORDER BY CODIGO_PEDIDO, CODIGO_PRODUTO;

-- /* 05 � Mostre os Produtos cujo VALOR_UNITARIO sejam inferiores a R$100, ordene por CODIGO_PRODUTO. */

-- SELECT * FROM PRODUTO 
-- WHERE VALOR_UNITARIO < 100
-- ORDER BY CODIGO_PRODUTO;

-- /*06 � Pesquise a quantidade de Pedidos realizadas
-- por Clientes, ordene a pesquisa por: CODIGO_CLIENTE e Quantidade de pedidos! */

-- SELECT COUNT(CODIGO_CLIENTE) AS QTD FROM PEDIDO
-- GROUP BY CODIGO_CLIENTE
-- ORDER BY CODIGO_CLIENTE, QTD;

-- /* 07 � Pesquise a quantidade de Clientes por unidade da federa��o, ordene a pesquisa por: UF e Quantidade de clientes! */

-- SELECT UF , COUNT(UF) QTD FROM CLIENTE
-- GROUP BY UF 
-- ORDER BY UF, QTD

-- /* 08 � Calcule a m�dia do valor unit�rio por unidade de medida, ordene a pesquisa por: Unidade e Valor m�dio! */

-- SELECT UNIDADE, ROUND(AVG (VALOR_UNITARIO), 1) AS MEDIA_POR_UNIDADE FROM PRODUTO
-- GROUP BY UNIDADE
-- ORDER BY UNIDADE , MEDIA_POR_UNIDADE

-- /* 09 � Calcule o menor, a m�dia, o maior sal�rio e total de sal�rios
-- por faixa de comiss�o no cadastro de Vendedores, ordene a pesquisa por: Faixa de comiss�o! */

-- SELECT FAIXA_COMISSAO, MIN(SALARIO) AS MENOR, CAST(AVG(SALARIO) AS DECIMAL (10,2)) AS MEDIA, MAX(SALARIO) AS MAIOR FROM VENDEDOR
-- GROUP BY FAIXA_COMISSAO
-- ORDER BY FAIXA_COMISSAO;

-- /* 10 � Calcule o menor, a m�dia e o maior prazo de entrega por vendedor, ordene a pesquisa por: C�digo do vendedor! */
-- SELECT CODIGO_VENDEDOR,
-- MIN(PRAZO_ENTREGA) AS MENOR_PRAZO,
-- AVG (PRAZO_ENTREGA) AS MEDIA_DE_PRAZO,
-- MAX (PRAZO_ENTREGA) AS MAIOR_PRAZO 
-- FROM PEDIDO
-- GROUP BY CODIGO_VENDEDOR
-- ORDER BY CODIGO_VENDEDOR

-- /* 11 � Calcule o menor, a m�dia e o maior prazo de entrega por cliente, ordene a pesquisa por: C�digo do cliente! */
-- SELECT CODIGO_CLIENTE,
-- MIN(PRAZO_ENTREGA) AS MENOR_PRAZO,
-- AVG (PRAZO_ENTREGA) AS MEDIA_DE_PRAZO,
-- MAX (PRAZO_ENTREGA) AS MAIOR_PRAZO 
-- FROM PEDIDO
-- GROUP BY CODIGO_CLIENTE
-- ORDER BY CODIGO_CLIENTE

-- /* 12. Liste todos os clientes que tenham o numero 5 como segundo caractere do CPF; */
-- SELECT * FROM CLIENTE
-- WHERE SUBSTRING(CPF,2,1) = '5'

-- SELECT * 
-- FROM CLIENTE
-- WHERE CPF LIKE '_5%';

-- /* 13. Liste todos os clientes que tenham o numero 99 como qualquer posi��o do CPF; */

-- SELECT * FROM CLIENTE
-- WHERE CPF LIKE '%99%'




-- /* Cria��o de tabela */

-- CREATE TABLE Pessoas (
--     Id INT PRIMARY KEY,
--     Nome VARCHAR(50) NOT NULL,
--     Sobrenome VARCHAR(50) NOT NULL,
--     Idade SMALLINT NOT NULL
-- );

-- select * from Pessoas


-- CREATE TABLE Funcionarios (
--     FuncionarioId INT PRIMARY KEY,
--     Nome VARCHAR(50) ,
--     Cargo VARCHAR(50) ,
--     DataContratacao DATE ,
--     Salario DECIMAL(10, 2) NOT NULL
-- );

-- select * from Funcionarios

-- CREATE TABLE Pedidos (
--     PedidoId INT not null PRIMARY KEY,
--     ClienteId INT NOT NULL,
--     DataPedido DATE NOT NULL,
--     ValorTotal DECIMAL(10, 2) NOT NULL
-- );

-- select * from Pedidos