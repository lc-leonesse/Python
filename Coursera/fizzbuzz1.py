"""
Exercícios 2 - FizzBuzz parcial, parte 1

Receba um número inteiro na entrada e imprima

Fizz

se o número for divisível por 3. Caso contrário, imprima o mesmo número que foi dado na entrada.

"""

numero = int(input("Informe um número: "))

divisao = numero % 3

if divisao == 0:
    print("Fizz")
else:
    print(numero)
