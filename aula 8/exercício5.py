#Faça um programa q fale quais dos 20 primeiros multiplos de 5 são pares
for i in range(5,101,5):
    if(i % 2 == 0):
        print(i)
        
#Some os impares e mostre essa soma no final
soma = 0
for i in range(5,101,5):
    if(i % 2 != 0):
        print(i)
        soma += i
print(f"A soma dos impares deu: {soma}")
 
       
    