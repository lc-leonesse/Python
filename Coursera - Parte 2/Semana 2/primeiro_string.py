"""

Escreva uma função que recebe um array de strings como parâmetro e
devolve o primeiro string na ordem lexicográfica, ignorando-se letras
maiúsculas e minúsculas


"""

def primeira_string(lista_de_strings):
    lista = []
    for x in lista_de_strings:
        a = x.lower()
        b = a.strip()
        c = b.split(' ')
        if len(c) > 1:
            d = str(c[0] + c[len(c)-1])
            lista.append(d)
        else:
            e = c[0]
            lista.append(e)
    lista.sort()
    menor = lista[0]
    return menor


lista_de_strings = ['ANABELE   ', ' adai  lton', ' josé', 'ferreir a', 'carlos', 'alfre do', 'zebu', 'aILTON']

print(primeira_string(lista_de_strings))


