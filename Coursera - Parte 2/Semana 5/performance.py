"""

Verifica a performance entre os algoritmos de Selection Sort e Bubble
Sort

"""

import random
import ordenadores
import time


class ContaTempos:
    def lista_aleatoria(self, n):
        lista = [0 for x in range(n)]
        for i in range(n):
            lista[i] = random.randrange(1000) # inteiros aleatórios entre 0 e 999
        return lista

    def compara(self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:]

        o = ordenadores.Ordenador()

        antes = time.time()
        o.bolha(lista1)
        depois = time.time()
        print("Bolha demorou", depois - antes)

        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print("Seleção direta demorou", depois - antes)

