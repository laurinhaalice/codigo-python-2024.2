# Programa para mostrar os 10 primeiros números da sequência da Fibnacci

numero1 = 1
numero2 = 1

print(numero1)
print(numero2)

for i in range(8):
    proximo = numero1 + numero2
    print(proximo)
    numero1 = numero2
    numero2 =  proximo

# Segunda forma:
    
a = 1
b = 1
pulo = 1
for i in range(10):
    pulo = b - a  # Atualiza 'pulo' com a distância entre os números
    temp = a      # Armazena o valor atua de '' em uma variável temporária
    a = b         # Atualiza 'a' com o valor de 'b' 
    b = temp + b  # Atualiza 'b' com a soma do antigo 'a' e 'b'