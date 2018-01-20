"""

Escreva a função soma_elementos que recebe como parâmetro uma lista com números inteiros e devolve um número inteiro
correspondente à soma dos elementos da lista recebida.

"""


def soma_elementos(lista):
    comprimento = len(lista)
    soma = 0
    for x in lista[0:comprimento:1]:
        soma = x + soma
    return soma



