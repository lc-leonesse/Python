"""

Matrizes

"""


def cria_matriz(num_linhas, num_colunas, valor):
    matriz = []
    for i in range(num_linhas):
        # cria a linha 1
        linha = []  # lista vazia
        for j in range(num_colunas):
            linha.append(valor)

        # adioiona linha à matriz
        matriz.append(linha)

    return matriz