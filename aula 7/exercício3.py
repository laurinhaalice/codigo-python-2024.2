# peça um numero ao usuario
numero = int(input("entre com um numero"))
# uso uma variavel de apoio que definira se um numero é primo ou não
primo = True
# faço um loop que va do numero 2 ate o antecessor a ele
for i in range(2, numero):
    # se um numero for divisivel pr qualquer numero sem ser 1 ou ele mesmo, primo será falso
    if(numero%i==0):
        primo = False
#se primo for falso é porque ele é divisivel por mmas algum numero sem ser 1 e ele mesmo9
if(primo==False):
    print("esse numero não é primo")
else:
    print("esse numero é primo")