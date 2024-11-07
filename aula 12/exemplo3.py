#Faça um programa que simule o armário de uma escola e permita colocar o nome do aluno responsavel/pagante da gaveta. O armário tem a dimensão 5x5.

matriz1=[
    [" ", " ", " ", " "],
    [" ", "PEDRO", " "],
    ["", "", "", "", ""],
    ["", "", "", "", ""],
    ["", "", "", "", ""]
]

#for linha in matriz:
#linha

#A escola adcionou um novo armario 3x3 perto das salas de aula e o chamou de armário vip. 
#Caso o aluno adquira uma gaveta no armário comum, custará 30,00 ao mes, o vip custará 50,00.
#Adcione no sistema essa seleção e retorne para o unsuario o custo.
    
matriz2=[
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

print("Para o armário comum, o preço é 30,00")
print("Para o armário vip, o preço é 50,00")
armario = input("Digite a escolha (1 ou 2): ")
nome = input("Qual o seu nome? ")
linha = int(input("Em qual linha do armário será sua gaveta? "))
coluna = int(input("Em qual coluna do armário será sua gaveta? "))
if armario == '1':
    matriz1[linha][coluna] = nome
    for linha in matriz1:
        print(linha)
elif armario == '2':
    matriz2[linha][coluna] = nome
    for linha in matriz2:
        print(linha)
    else:
        print("armario não identificado")
    

    