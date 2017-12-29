"""

Raiz Quadrática utilizando funções

"""


import math

def delta(a, b, c):
    return (b**2) - (4 * a * c)

def main():
    a = float(input("Informe o primeiro valor (a): "))
    b = float(input("Informe o segundo valor (b): "))
    c = float(input("Informe o terceiro valor (c): "))
    imprime_raizes(a, b, c)

def imprime_raizes(a, b, c):
    d = delta(a, b, c)
    if d > 0:
        x = ((-b) + math.sqrt(d)) / (2 * a)
        y = ((-b) - math.sqrt(d)) / (2 * a)
        if x < y:
            print("as raízes da equação são", x, "e", y)
        else:
            print("as raízes da equação são", y, "e", x)
    if d < 0:
        print("esta equação não possui raízes reais")
    if d == 0:
        x = ((-b) + math.sqrt(d)) / (2 * a)
        print("a raiz desta equação é", x)



