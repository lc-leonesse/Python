"""

Refatoração do programa de Bhaskara, utilizando Orientação a Objeto

"""

import math


class Bhaskara:
    def main(self):
        a = float(input("Informe o primeiro valor (a): "))
        b = float(input("Informe o segundo valor (b): "))
        c = float(input("Informe o terceiro valor (c): "))
        print(self.calcula_raizes(a, b, c))

    def delta(self, a, b, c):
        return (b**2) - (4 * a * c)

    def calcula_raizes(self, a, b, c):
        d = self.delta(a, b, c)
        if d > 0:
            x = ((-b) + math.sqrt(d)) / (2 * a)
            y = ((-b) - math.sqrt(d)) / (2 * a)
            return 2, x, y
        if d < 0:
            return 0
        if d == 0:
            x = ((-b) + math.sqrt(d)) / (2 * a)
            return 1, x






