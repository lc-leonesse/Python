"""

Ainda na classe Triangulo,

Caso positivo, o método deve devolver True. Caso negativo, deve
devolver False.

Verifique a semelhança dos triângulos através do comprimento dos lados.

Dica: você pode colocar os lados de cada um dos triângulos em uma lista
diferente e ordená-las.

"""

def main():
    t1 = Triangulo(2,2,2)
    t2 = Triangulo(4,4,4)
    t1.semelhantes(t2)


class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def semelhantes(triangulo):













