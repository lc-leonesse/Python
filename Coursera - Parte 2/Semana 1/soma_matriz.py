"""

Escreva a função soma_matrizes(m1, m2) que recebe 2 matrizes e devolve uma matriz que represente sua soma caso
as matrizes tenham dimensões iguais. Caso contrário, a função deve devolver False.

m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]
soma_matrizes(m1, m2) => [[3, 5, 7], [9, 11, 13]]

m1 = [[1], [2], [3]]
m2 = [[2, 3, 4], [5, 6, 7]]
soma_matrizes(m1, m2) => False

"""


def soma_matrizes(m1, m2):
    if(len(m1) != len(m2) or len(m1[0]) != len(m2[0])):
        return False
    result = []
    for i in range(len(m1)):
        result.append([])
        for j in range(len(m1[0])):
            result[i].append(m1[i][j] + m2[i][j])
    return result
