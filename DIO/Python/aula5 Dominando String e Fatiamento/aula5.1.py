nome = "joao pedro"
idade = 20
profissão = 'Programador'
Linguagem = "Python"

print('Ola me chamo %s. Eu tenho %d anos de idade , trabalho como %s e estou matriculado da dio do curso de {}.'.format(nome,idade,profissão,Linguagem))


print('Ola me chamo {0}. Eu tenho {1} anos de idade , trabalho como {2} e estou matriculado da dio do curso de {3}.'.format(nome,idade,profissão,Linguagem))

print(f'Ola me chamo {nome}. Eu tenho {idade} anos de idade , trabalho como {profissão} e estou matriculado da dio do curso de {Linguagem}.'.format(nome,idade,profissão,Linguagem))


pi = 3.14429411241

print(f'{pi:.2f} ,pi' ) #O código print(f'{pi:.2f}, pi') irá exibir o valor de 'pi' formatado com duas casas decimais.
print(f'{pi:10.2f} ,pi' ) #Se 'pi' for 3.14159, a saída será "      3.14, pi" (com espaços em branco para alcançar 10 caracteres).
