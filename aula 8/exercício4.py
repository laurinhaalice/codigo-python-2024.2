soma = 0
for i in range(4):
    número = float(input("Insira um número:"))
    if número % 2 != 0:
        soma += número

print(f"A soma dos números impares deu:{soma}")