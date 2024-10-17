import random

# Gera um número inteiro aleatório entre 1 e 100
numeroaleatorio = random.randint(1, 100)
print(f"Número intero aleatório entre 1 e 100: {numeroaleatorio}")

print("Entre com dois números , irei retornar um número aleatório entre eles")
numerousuriomenor = int(input("Entre com o menor deles:"))
numerousuariomaior = int(input("Entre com o maior deles:"))
numeroaleotario2 = random.randint(numerousuriomenor, numerousuariomaior)

print(f"Número inteiro aleatório entre {numerousuriomenor} e {numerousuariomaior}:{numeroaleotario2}")