"""

Como pedido na primeira video-aula desta semana, escreva um programa que recebe uma sequência de números inteiros
terminados por 0 e imprima todos os valores em ordem inversa. Note que 0 (ZERO) não deve fazer parte da sequência.

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


numero = int(input("Digite um número: "))


while numero != 0:
    lista.append(numero)
    numero = int(input("Digite um número: "))
    if numero == 0:
        print(lista[::-1])  # lista do final para o início. Step = -1
