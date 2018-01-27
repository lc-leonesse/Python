"""

Escreva a função lista_grande(n), que recebe como parâmetro um
número inteiro n e devolve uma lista contendo n números inteiros
aleatórios.

"""

import random


def lista_grande(n):

    lista = random.sample(range(0, n), n)

    return lista


