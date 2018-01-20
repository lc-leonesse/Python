"""

Escreva uma função dimensoes(matriz) que recebe uma matriz como parâmetro e imprime as dimensões da matriz recebida,
no formato iXj.

Exemplos:

minha_matriz = [[1], [2], [3]]
dimensoes(minha_matriz)
3X1

minha_matriz = [[1, 2, 3], [4, 5, 6]]
dimensoes(minha_matriz)
2X3


"""


def dimensoes(minha_matriz):
    tamanho = (len(minha_matriz), len(minha_matriz[0]))
    print('{}x{}'.format(tamanho[0], tamanho[1]))


