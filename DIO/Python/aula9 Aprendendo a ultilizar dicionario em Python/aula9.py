pessoa = {"nome": "Guilherme", "idade":28}

pessoa = dict(nome ="guilherme",idade=28)

pessoa["telefone"] = "3333-1234" # {"nome": "Guiçherme", "idade": 28, "telefone":3333-1234} 

print(pessoa)

dados = {"nome": "Guilhermer","idade":28,"telefone":"3333-1234" }
print('')
dados["nome"]
dados["idade"]
dados["telefone"]
# {'nome': 'Guilhermer', 'idade': 28, 'telefone': '3333-1234'}

print (dados)

dados["nome"] ="Maria"
dados["idade"]= 18
dados["telefone"] = "9988-1781"
print('')
#{'nome': 'Maria', 'idade': 18, 'telefone': '9988-1781'}
print (dados)

## Dicionário alinhado

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121 "},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

print(contatos)
print('')
print('')
telefone = contatos["giovanna@gmail.com"]["telefone"]  # "3443-2121"
print(telefone)

## interando o dicionario

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

### resultado 1

for chave in contatos:
    print(chave, contatos[chave])

print("=" * 100)
### resultado 2
for chave, valor in contatos.items():
    print(chave, valor)
