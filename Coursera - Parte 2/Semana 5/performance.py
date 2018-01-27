"""

Verifica a performance entre os algoritmos de Selection Sort e Bubble
Sort

"""

import random
import time
import ordenador

class ContaTempos:
    def lista_aleatoria(self, n):
        lista = [0 for x in range(n)]
        for i in range(n):
            lista[i] = random.randrange(1000) # inteiros aleatórios entre 0 e 999
        return lista

    def compara(self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:]

        o =