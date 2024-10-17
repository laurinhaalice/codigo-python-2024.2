import random
numeroaleatorio = random.randint(1, 200)
print("Qual o nível de dificuldade você gostaria de jogar?")
print("1 - Fácil (10 tentativas)")
print("2 - Médio (7 tentativas)")
print("3 - Difícil (5 tentativas)")

nivel = input("Escolha o nível de dificuldade (1, 2 ou 3): ")

if nivel == '1':
    tentativas = 10
elif nivel == '2':
    tentativas = 7
elif nivel == '3':
    tentativas = 5
else:
    print("Nível inválido")
    exit()
for i in range(1, tentativas + 1):
    palpite = int(input("Entre com um palpite:"))
    if palpite == numeroaleatorio:
        print("Parabéns, você acertou o palpite")
        break
    else:
        print("Você errou o seu palpite.")
    if palpite <= numeroaleatorio:
            print("O palpite é maior que o número aleatório.")
    elif palpite >= numeroaleatorio:
        print("Seu palpite é menor que o número aleatório.")
    elif palpite == numeroaleatorio:
        print("Seu palpite é igual ao número aleatório.")
        break
print(f"Este é o número aleatório: {numeroaleatorio}")
