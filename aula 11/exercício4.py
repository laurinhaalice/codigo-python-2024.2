# faça uma função chamada converter. Essa função deve receber uma temperatura em celcius e retornar em fahrenheit.
def converter(celsius):
   fahrenheit = celsius * 9/5+32
   return fahrenheit
temperatura = float(input("Coloque uma temperatura: "))
resultado = converter(temperatura)
print(f"O resultado de fahrenheit é: {resultado}°F")