"""

Mede a performance das Buscas Binária e Sequencial em uma lista grande

"""

import time
import random

def busca_binaria(lista, x):
    primeiro = 0
    ultimo = len(lista) - 1

    while primeiro <= ultimo:
        meio = (primeiro + ultimo)//2
        if lista[meio] == x:
            return meio
        else:
            if x < lista[meio]:
                ultimo = meio - 1
            else:
                primeiro = meio + 1
    return -1

def busca_sequencial(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return False

def lista_sequencial(n):
    lista = [x for x in range(n)]
    return lista


def compara(n, x):
    lista = lista_sequencial(n)



    print('Comparando com lista aleatória')
    print('\nBusca Binária')
    antes = time.time()
    busca_binaria(lista, x)
    depois = time.time()
    print('Busca Binária levou ', depois - antes, 'segundos')

    print('\nBusca Sequencial')
    antes = time.time()
    busca_sequencial(lista, x)
    depois = time.time()
    print('Busca Sequencial levou', depois - antes, 'segundos')










