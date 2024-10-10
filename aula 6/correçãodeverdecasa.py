
soma = 0
contador = 0

# Solicita ao usuário que insira 5 números
while contador < 5:
    numero = float(input("insira um número:"))
    soma += numero
    contador += 1

# Exibe a soma total 
print("A soma total é:" , soma)
