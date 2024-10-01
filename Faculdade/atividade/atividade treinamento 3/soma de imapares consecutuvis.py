def soma_impares(x, y):
    soma = 0
    for i in range(min(x, y)+1, max(x, y)):
        if i % 2 != 0:
            soma += i
    return soma
x = int(input())
y = int(input())
print(soma_impares(x, y))