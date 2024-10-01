import requests

def consulta_cep(cep):
    # Define a URL da API com o CEP fornecido
    url = f"https://viacep.com.br/ws/{cep}/json/"
    
    # Faz a requisição GET para a API
    resposta = requests.get(url)
    
    # Verifica se a resposta foi bem-sucedida
    if resposta.status_code == 200:
        # Converte a resposta JSON para um dicionário Python
        dados = resposta.json()
        
        # Verifica se o CEP é válido
        if 'erro' not in dados:
            return dados
        else:
            return "CEP inválido."
    else:
        return "Erro na consulta."

# Exemplo de uso
cep = "03361010"

resultado = consulta_cep(cep)
print(resultado)
