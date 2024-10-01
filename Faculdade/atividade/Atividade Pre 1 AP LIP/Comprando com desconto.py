preco = float(input())
quantidade = int(input())

desconto = (quantidade + 10) /100
valor = preco * quantidade
valorD = (preco * quantidade) * (1.00 - desconto )

print(f"{valor:.2f}")
print(f"{valorD:.2f}")
