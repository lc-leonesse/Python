"""
Escreva um programa que recebe como entradas (utilize a função input)
dois números inteiros correspondentes à largura e à altura de um
retângulo, respectivamente. O programa deve imprimir uma cadeia de
caracteres que represente o retângulo informado com caracteres '#'
na saída.

Por exemplo:

digite a largura: 10
digite a altura: 3

##########
##########
##########

digite a largura: 2
digite a altura: 2
##
##

"""


largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

simbolo = "#"
n = 1

while n <= altura:
    print(simbolo * largura)
    altura = altura -1


