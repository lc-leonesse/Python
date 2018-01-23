"""

Como pedido no segundo vídeo da semana, escreva a função
primeiro_lex(lista) que recebe uma lista de strings como parâmetro e
devolve o primeiro string na ordem lexicográfica. Neste exercício,
considere letras maiúsculas e minúsculas.

Dica: revise a segunda vídeo-aula desta semana.


"""

def primeiro_lex(lista):
    lista_nova = [] 
    for x in lista:
        b = x.strip()
        c = b.split(' ')
        if len(c) > 1:
            d = str(c[0] + c[len(c)-1])
            lista_nova.append(d)
        else:
            e = c[0]
            lista_nova.append(e)
    lista_nova.sort()
    menor = lista_nova[0]
    return menor







