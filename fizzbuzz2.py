"""
Exercícios 3 - FizzBuzz parcial, parte 2

Receba um número inteiro na entrada e imprima

Buzz

se o número for divisível por 5. Caso contrário, imprima o mesmo número que foi dado na entrada.

"""

numero = int(input("Informe um número: "))

divisao = numero % 5

if divisao == 0:
    print("Buzz")
else:
    print(numero)
