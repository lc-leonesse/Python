"""
Exercícios 4 - FizzBuzz parcial, parte 3

Receba um número inteiro na entrada e imprima

FizzBuzz

na saída se o número for divisível por 3 e por 5. Caso contrário, imprima o mesmo número que foi dado na entrada.

"""


numero = int(input("Informe um número: "))

divisao3 = numero % 3

divisao5 = numero % 5

if divisao3 == 0 and divisao5 == 0:
    print("FizzBuzz")
else:
    print(numero)
