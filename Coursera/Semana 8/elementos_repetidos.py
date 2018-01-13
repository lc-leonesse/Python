"""

Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros, verifica se tal
lista possui elementos repetidos e os remove. A função deve devolver uma lista correspondente à primeira lista,
sem elementos repetidos. A lista devolvida deve estar ordenada.

Dica: Você pode usar lista.sort() ou sorted(lista). Qual a diferença?

"""


def remove_repetidos(lista):
    for x in lista[0:(len(lista)):1]:
        contador = lista.count(x)
        if contador > 1:
            indice = lista.index(x)
            del lista[indice]
    lista = lista.sort()
    return lista









