import random

numero1 = random.uniform(20,50)
numero2 = random.uniform(20,50)
numero3 = random.uniform(20,50)
numero4 = random.uniform(20,50)
loop = 1
print(numero1, numero2, numero3, numero4)
while (loop == 1):
    if numero2 > numero1:
        auxiliar = numero1 
        numero1 = numero2
        numero1 = auxiliar
    
    if numero3 > numero2:
        auxiliar = numero2
        numero2 = numero3
        numero3 = auxiliar
    
    if numero4 > numero3:
        auxiliar = numero3
        numero3 = numero4
        numero4 = auxiliar
    if numero4 < numero3 and numero3 < numero2 and numero2 < numero1:
        print(f"Essa é a ordem {numero1} {numero2} {numero3} {numero4}")
        loop+=1