"""

Implementar uma função para multiplicar matrizes

Regra para multiplicação de matrizes:
O número de colunas da primeira Matriz deve ser igual ao número de linhas
da segunda Matriz

"""

def multiplica_matriz(A,B):
    num_linhas_A, num_colunas_A = len(A), len(A[0])
    num_linhas_B, num_colunas_B = len(B), len(B[0])
    assert num_linhas_A == num_colunas_B

    C = []
    for linha in range(num_linhas_A):
        # começando uma nova linha
        C.append([])
        for coluna in range(num_colunas_B):
            # adicionando uma nova coluna na linha
            C[linha].append(0)
            for k in range(num_colunas_A):
                C[linha][coluna] += A[linha][k] * B[k][coluna]
    return C

if __name__ == '__main__':
    A = [[1,2,3],[4,5,6]]
    B = [[1,2],[3,4],[5,6]]
    print(multiplica_matriz(A,B))

