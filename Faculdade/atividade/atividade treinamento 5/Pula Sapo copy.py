def verifica_jogo(P, N, canos):
    for i in range(N-1):
        if abs(canos[i] - canos[i+1]) > P:
            return "GAME OVER"
    return "YOU WIN"
# Exemplo de uso
P, N = map(int, input().split())
canos = list(map(int, input().split()))
print(verifica_jogo(P, N, canos))
