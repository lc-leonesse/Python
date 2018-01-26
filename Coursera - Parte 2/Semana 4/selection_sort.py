"""

Implemente a função ordena(lista), que recebe uma lista com números
inteiros como parâmetro e devolve esta lista ordenada.
Utilize o algoritmo selection sort.

"""

def ordena(lista):
    for i in range(len(lista)-1):
        minimo = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[minimo]:
                minimo = j

        lista[i], lista[minimo] = lista[minimo], lista[i]

    return lista


