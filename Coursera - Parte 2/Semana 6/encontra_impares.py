"""

Implemente a função encontra_impares(lista), que recebe como
parâmetro uma lista de números inteiros e devolve uma outra lista
apenas com os números ímpares da lista dada.

Sua solução deve ser implementada utilizando recursão.

Dica: você vai precisar do método extend() que as listas possuem.

"""

def encontra_impares(lista):
    lista_nova = []
    if len(lista) > 0:
        numero = lista.pop(0)

        if numero % 2 != 0:
            lista_nova.append(numero)
        lista_nova = lista_nova + encontra_impares(lista)
    return lista_nova












