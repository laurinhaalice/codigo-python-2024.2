def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero não é permitida."

# Função principal da calculadora
def calculadora():
    print("selecione a opção:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    escolha = input("Digite a escolha (1/2/3/4): ")

    if escolha in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print(f"O resultado da soma é: {somar(num1, num2)}")
        elif escolha == '2':
            print(f"O resultado da subtração é: {subtrair(num1, num2)}")
        elif escolha == '3':
            print(f"O resultado da multiplicação é: {multiplicar(num1, num2)}")
        elif escolha == '4':
            print(f"O resultado da divisão é: {dividir(num1, num2)}")
    else:
        print("Escolha inválida. Por favor, tente novamente.")

# Executando a calculadora
calculadora()