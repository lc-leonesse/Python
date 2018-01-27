"""

Implementação do algorítmo Insertion Sort

"""


def insertion_sort(lista):
    for indice in range(1, len(lista)):

        valor_atual = lista[indice]
        posicao = indice

        while posicao > 0 and lista[posicao-1] > valor_atual:
            lista[posicao] = lista[posicao-1]

        lista[posicao] = valor_atual

    return lista






lista = [14,46,43,27,57,41,45,21,70]

print(insertion_sort(lista))