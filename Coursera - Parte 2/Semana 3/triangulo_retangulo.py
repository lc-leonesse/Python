"""

Escreva, na classe Triangulo, o método retangulo() que devolve True
se o triângulo for retângulo, e False caso contrário.

"""


class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def retangulo(self):
        if self.a > self.b and self.a > self.c:
            if self.a ** 2 == (self.b ** 2) + (self.c ** 2):
                return True
            else:
                return False
        if self.b > self.a and self.b > self.c:
            if self.b ** 2 == (self.a ** 2) + (self.c ** 2):
                return True
            else:
                return False
        if self.c > self.a and self.c > self.b:
            if self.c ** 2 == (self.a ** 2) + (self.b ** 2):
                return True
            else:
                return False
        if self.a == self.b == self.c:
            return False
