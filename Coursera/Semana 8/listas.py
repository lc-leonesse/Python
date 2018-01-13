"""

Lê uma sequeência de números do teclado. Quanso o usuário digitar 0, imprimir a lista em ordem inversa a digitada
pelo usuário

lista[start:end:step] - slice

a[start:end] # items start through end-1
a[start:]    # items start through the rest of the array
a[:end]      # items from the beginning through end-1
a[:]         # a copy of the whole array

a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items

"""


lista = []


numero = int(input("Informe um número. Para terminar, informe 0 (zero): "))


while numero != 0:
    lista.append(numero)
    numero = int(input("Informe um número. Para terminar, informe 0 (zero): "))
    if numero == 0:
        print(lista[::-1])  # lista do final para o início. Step = -1
