"""

Casos de teste usando parametrize

"""

import pytest
import Bhaskara



@pytest.fixture
def b():
    return Bhaskara.Bhaskara()


@pytest.mark.parametrize('entrada, esperado', [
    ( (1, 0, 0), (1,0) ),
    ( (1, -5, 6), (2, 3, 2) ),
    ( (10, 10, 10),  0),
    ( (10, 20, 10), (1, -1) )
    ] )
def testa_raiz(b, entrada, esperado):
    assert b.calcula_raizes(entrada) == esperado
