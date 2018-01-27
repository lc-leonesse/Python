"""

Implemente a função insertion_sort(lista), que recebe uma lista
com números inteiros como parâmetro e devolve esta lista ordenada.
Utilize o algoritmo insertion sort.

"""


def insertion_sort(lista):
    for indice in range(1, len(lista)):

        valor_atual = lista[indice]
        posicao = indice

        while posicao > 0 and lista[posicao-1] > valor_atual:
            lista[posicao] = lista[posicao-1]
            posicao = posicao - 1

        lista[posicao] = valor_atual

    return lista








