"""

Escreva a função ordenada(lista), que recebe uma lista com números
inteiros como parâmetro e devolve o booleano True se a lista estiver
ordenada e False se a lista não estiver ordenada.

"""

def ordenada(lista):
    a = []
    for x in lista:
        a.append(x)
    a.sort()
    if lista == a:
        return True
    else:
        return False

