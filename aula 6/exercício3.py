x = True
soma = 0
while (x==True):
    numero = float(input("Digite um número:"))
    continuar = input("Continuar ou parar?").lower()
    if (continuar == "parar"):
          x = False
          print(f"A soma deu:{soma}")
    else:
         soma += numero