"""# Entrada de dados
P, N = map(int, input().split())
alturas = list(map(int, input().split()))""""""

# Inicializa a variável de resultado como "YOU WIN"
resultado = "YOU WIN"

# Verifica cada par de alturas consecutivas
for i in range(len(alturas) - 1):
    if alturas[i+1] - alturas[i] > P:
        resultado = "GAME OVER"
        break

print(resultado)"""

def pode_vencer(P, N, alturas):
    # Verifica se a primeira altura é maior que P
    if alturas[0] > P:
        return "GAME OVER"
    
    # Inicializa a plataforma atual com a primeira altura
    plataforma_atual = alturas[0]
    
    # Itera sobre as plataformas restantes
    for i in range(1, N):
        # Verifica se a próxima plataforma é inalcançável
        if alturas[i] > plataforma_atual + P:
            return "GAME OVER"
        
        # Atualiza a plataforma atual para a mais alta alcançável
        plataforma_atual = min(alturas[i], plataforma_atual + P)
    
    # Retorna "YOU WIN" se todas as plataformas forem alcançáveis
    return "YOU WIN"

# Função principal
def main():
    # Entrada de dados
    P, N = map(int, input("").split())
    alturas = list(map(int, input("").split()))

    # Chama a função pode_vencer e imprime o resultado
    resultado = pode_vencer(P, N, alturas)
    print(resultado)

# Chama a função principal se o script for o principal executado
if __name__ =="__main__":
    main()
