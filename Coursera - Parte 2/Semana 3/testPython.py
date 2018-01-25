
import pytest

def soma(a, b, c):
    resultado = a + b + c
    return resultado

@pytest.mark.parametrize('a, b, c, esperado', [
    (1,2, 3, 6),
    (3, 4, 5, 12),
    (4, 5, 6, 15),
    (10, 34, 40, 84)
])

def testa_soma(a,b,c, esperado):
    assert soma(a,b,c) == esperado


