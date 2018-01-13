"""

Lê uma sequeência de números do teclado. Quanso o usuário digitar 0, imprimir a lista em ordem inversa a digitada
pelo usuário


"""


lista = []

numero = int(input("Informe um número. Para terminar, informe 0 (zero): "))

while numero != 0:
    lista.append(numero)
    if numero == 0:
        comprimento = len(lista)
        print(lista[])