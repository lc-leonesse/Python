"""

Testes automatizados dos ordenadores (Bubble Sort e Selection Sort)

"""

import ordenadores
import pytest
import performance


class TestaOrdenador:

    @pytest.fixture
    def o(self):
        return ordenadores.Ordenador()

    @pytest.fixture
    def l_quase(self):
        c = performance.ContaTempos()
        return c.lista_quase_ordenada(100)

    @pytest.fixture
    def l_aleatoria(self):
        c = performance.ContaTempos()
        return c.lista_aleatoria(100)

    def esta_ordenada(self,l):
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                return False
        return True

    def test_bolha_curta_aleatoria(self,o,l_aleatoria):
        o.bolha_curta(l_aleatoria)
        assert self.esta_ordenada(l_aleatoria)

    def test_selecao_direta_aleatoria(self,o,l_aleatoria):
        o.selecao_direta(l_aleatoria)
        assert self.esta_ordenada(l_aleatoria)

    def test_bolha_curta_quase(self, o, l_quase):
        o.bolha_curta(l_quase)
        assert self.esta_ordenada(l_quase)

    def test_selecao_direta_quase(self, o, l_quase):
        o.selecao_direta(l_quase)
        assert self.esta_ordenada(l_quase)



