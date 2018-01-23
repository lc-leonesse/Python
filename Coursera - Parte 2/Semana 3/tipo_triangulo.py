"""

Na classe triângulo, definida na Questão 1, escreva o metodo tipo_lado()
que devolve uma string dizendo se o triângulo é:

isósceles (dois lados iguais)

equilátero (todos os lados iguais)

escaleno (todos os lados diferentes)

Note que se o triângulo for equilátero, a função não deve devolver
isóceles.

"""

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def tipo_lado(self):
        if self.a == self.b and self.a == self.c and self.b == self.c:
            return 'equilátero'
        if self.a == self.b and self.a == self.b and self.b != self.c:
            return 'isósceles'
        if self.a != self.b and self.a != self.c and self.b != self.c:
            return 'escaleno'
