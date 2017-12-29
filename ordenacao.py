"""
Exercício 5 - Verificando ordenação

Receba 3 números inteiros na entrada e imprima

crescente

se eles forem dados em ordem crescente. Caso contrário, imprima

não está em ordem crescente

"""

a = int(input("Informe o primeiro número: "))
b = int(input("Informe o segundo número: "))
c =  int(input("Informe o terceiro número: "))

if a < b < c:
    print("crescente")
else:
    print("não está em ordem crescente")