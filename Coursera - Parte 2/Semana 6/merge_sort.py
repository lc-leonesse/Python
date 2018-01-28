"""

Merge Sorte usando algoritmo recursivo
Merge Sort = ordenação por intercalação
- Divida a lista na metade recursivamente, até que cada sublista contenha
apenas 1 elemento (portando, já ordenada).
- Repetidamente, intercale as sublistas para produzir novas listas
ordenadas
- Repita até que tenhamos apenas 1 lista no final (que está ordenada).

"""


def merge_sort(lista):
    if len(lista) <= 1:     # base da recursão
        return lista

    meio = len(lista)//2

    lado_esquerdo = merge_sort(lista[:meio])
    lado_direito = merge_sort(lista[meio:])

    return merge(lado_esquerdo, lado_direito)


def merge(lado_esquerdo, lado_direito):
    if not lado_esquerdo:       # base da recursão
        return lado_direito
    if not lado_direito:            # base da recursão
        return lado_esquerdo

    if lado_esquerdo[0] < lado_direito[0]:
        return [lado_esquerdo[0]] + merge(lado_esquerdo[1:], lado_direito)

    return [lado_direito[0]] + merge(lado_esquerdo, lado_direito[1:])
