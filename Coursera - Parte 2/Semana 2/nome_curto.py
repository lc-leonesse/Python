"""

Escrever uma função que recebe uma lista de strings contendo nomes
de pessoas como parâmetro e devolve o nome mais curto. A função deve
 ignorar espaços antes e depois do nome e deve devolver o nome
 "capitalizado", i.e., apenas com a primeira letra maiúscula.

"""

def menor_nome(lista_de_nomes):
    lista_tamanho = []
    for x in lista_de_nomes:
        a = x.strip()
        tamanho = len(a)
        lista_tamanho.append(tamanho)
        menor = min(lista_tamanho)
        posicao = lista_tamanho.index(menor)
        curto = lista_de_nomes[posicao]
    return curto.strip().capitalize()






