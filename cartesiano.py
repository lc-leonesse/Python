"""
Exercício 1 - Distância entre dois pontos

Receba 4 números inteiros na entrada. Os dois primeiros devem corresponder, respectivamente, às coordenadas x e y de um
ponto em um plano cartesiano. Os dois últimos devem corresponder, respectivamente, às coordenadas x e y de um outro
ponto no mesmo plano.

Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10, imprima

longe

na saída. Caso o contrário, quando a distância for menor que 10, imprima

perto

"""

import math

xa = float(input("Informe o primeiro ponto: "))
ya = float(input("Informe o segundo ponto: "))
xb = float(input("Informe o terceiro ponto: "))
yb = float(input("Informe o quarto ponto: "))

"""
Cálculo das hipotenusas

A soma dos quadrados dos catetos é igual ao quadrado da hipotenusa
"""
ha = math.sqrt((xa ** 2) + (ya ** 2))
hb = math.sqrt((xb ** 2) + (yb ** 2))

if (hb-ha) >= 10:
    print("longe")
else:
    print("perto")