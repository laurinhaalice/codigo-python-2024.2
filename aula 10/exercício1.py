import random

numero1 = random.uniform(1, 15)
numero2 = random.uniform(1, 15)
numero3 = random.uniform(1, 15)

tentativa = float(input(f"Tente adivinhar o maior número 1, 2 ou 3:"))


if "1" == numero1 >numero2 and numero1 > numero3:
     print("Parabéns, você acertou!")   
elif "2" == numero2 >= numero2 > numero1 and numero2 > numero3:
    print("Parabéns, você acertou, o número 2 é o maior deles")
elif "3" == numero3 >= numero3 > numero2 and numero3 > numero1:
    print("Parabéns, você acertou, o número 3 é o maior deles")
else:
    print("Você errou, estes eram os números aleatórios:")
    print(f"1={numero1}")
    print(f"2={numero2}")
    print(f"3={numero3}")