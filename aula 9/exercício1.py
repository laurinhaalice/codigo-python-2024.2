jogar = True
while jogar: 
    contador = 0
    print("Kahoot iniciado.")
    pergunta1 = input("Tropicália foi um movimento da década de 60, onde os ideais dos artistas eram contra o Golpe Militar. E alguns dos artistas que participaram foram exilados. (Verdadeiro/Falso) ").lower()
    if pergunta1 == "verdadeiro":
        print("Você acertou!")
        contador += 1
    else:
        print("Você errou.")

    pergunta2 = input("Chico Buarque escrevia canções com mensagens subliminares contra o governo dessa época, uma delas seria: Canto de Ossanha, Garota de Ipanema e Chega de Saudade. (Verdadeiro/Falso) ").lower()
    if pergunta2 == "falso":
        print("Você acertou!")
        contador += 1
    else:
        print("Você errou.")

    pergunta3 = input("A cantora Rita Lee chegou a ser prea e visitada pea ilustríssima Elis Regina em 1976. (Verdadeiro/Falso)").lower()
    if pergunta3 == "verdadeiro":
        print("Você acertou!")
        contador += 1
    else:
        print("Você errou.")
    jogarnovamente = input("Você deseja jogar novamente? (sim/nao)")    
    if(jogarnovamente == "nao"):
        jogar = False
quantidadesdepergunta = 3
if(contador/2 < quantidadesdepergunta):
    print("Você venceu, parabéns!")
else:
    print("Não foi dessa vez!")
