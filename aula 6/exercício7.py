#peça 2 numeros e faça uma operação com base no seguinte menu, -1 soma dois numeros 2- subtrai dois numeros 3- multiplica dois numeros 4- dividir dois numeros

#peça ao cliente pra escolher uma operação
print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
    
operacao = int(input("Digite o número da operação desejada: "))
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
    
if operacao == 1:
        resultado = numero1 + numero2
        print(f" {numero1} x {numero2} = {resultado}.")
elif operacao == 2:
        resultado = numero1 - numero2
        print(f" {numero1} x {numero2} = {resultado}.")
elif operacao == 3:
        resultado = numero1 * numero2
        print(f" {numero1} x {numero2} = {resultado}.")
elif operacao == 4:
        if numero2 != 0:
            resultado = numero1 / numero2
            print(f" {numero1} x {numero2} = {resultado}.")
        else:
            print("Erro: Divisão por zero não é permitida.")
else:
        print("Operação inválida.")


