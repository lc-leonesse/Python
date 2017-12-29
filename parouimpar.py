"""
Exercício 1 - Par ou ímpar?

Receba um número inteiro na entrada e imprima

par

quando o número for par ou

ímpar

quando o número for ímpar.

"""

numero = int(input("Informe um número: "))

divisao = numero % 2

if divisao == 0:
    print("par")
else:
    print("ímpar")