numero = int(input("Digite um número: "))
contador = 1  

print(f"A tabuada do {numero} é:")
while contador <= 10:
    multiplica = numero * contador
    print(f"{numero} x {contador} = {multiplica}")
    contador += 1  