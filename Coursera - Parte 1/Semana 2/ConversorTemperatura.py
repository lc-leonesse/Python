"""

Conversor de temperatura (Celsius e Fahrenheit

"""

temp = float(input("Insira o valor da temperatura: "))
tipo = input("Informe (C)elsius ou (F)ahrenheit: ")

celsius = "c"
farenheit = "f"

if tipo == "f":
    conv = (((temp - 32) * 5) / 9)
    print("A temperatura informada é", int(conv), "graus celsius")

elif tipo == "c":
    conv = ((9 * temp) / 5) + 32
    print("A temperatura informada é", int(conv), "graus fahrenheit")

else:
    print("Informe um tipo de temperatura válido")
