"""

Matrizes

"""


def cria_matriz(num_linhas, num_colunas):
    """
    (int,int) -> matriz (lista de listas)
    Cria e retorna uma matriz com num_linhas linhas e num_colunas colunas em que cada elemento é
    digitado pelo usuário

    :param num_linhas: int
    :param num_colunas: int
    :return:
    """
    matriz = []
    for i in range(num_linhas):
        # cria a linha 1
        linha = []  # lista vazia
        for j in range(num_colunas):
            valor = int(input("Digite o elemento [" + str(i) + "][" + str(j) + "]"))
            linha.append(valor)

        # adioiona linha à matriz
        matriz.append(linha)

    return matriz



def le_matriz():
    lin = int(input("Digite o número de linhas da matriz: "))
    col = int(input("Digite o número de colunas da matriz: "))
    return cria_matriz(lin, col)
    



