def filtro(n):
    # Inicializa contadores para cada categoria
    epr = 0  # Alunos de Engenharia de Produção
    ehd = 0  # Alunos de Engenharia Hídrica
    intrusos = 0  # Alunos com cursos não reconhecidos

    # Itera sobre o número de alunos fornecido
    for i in range(n):
        # Lê a entrada do usuário para cada aluno, separando o número de matrícula e o curso
        num_matricula, curso = input().split()

        # Verifica o curso do aluno e atualiza os contadores apropriados
        if curso == 'EPR':
            epr += 1
        elif curso == 'EHD':
            ehd += 1
        else:
            intrusos += 1

    # Retorna a contagem de alunos de cada categoria
    return epr, ehd, intrusos

try:
    # Loop principal para continuar lendo a entrada até encontrar o final do arquivo (EOF)
    while True:
        # Lê o número de alunos na sala
        n = int(input())

        # Chama a função filtro para contar os alunos de cada categoria
        epr, ehd, intrusos = filtro(n)

        # Imprime o número de alunos de cada categoria
        print(f'EPR: {epr}')
        print(f'EHD: {ehd}')
        print(f'INTRUSOS: {intrusos}')

# Captura a exceção de final de arquivo (EOF) para encerrar o programa
except EOFError:
    pass
