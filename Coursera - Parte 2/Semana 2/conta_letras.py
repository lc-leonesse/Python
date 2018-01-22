"""
Escreva a função conta_letras(frase, contar="vogais"), que recebe como
primeiro parâmetro uma string contendo uma frase e como segundo
parâmetro uma outra string. Este segundo parâmetro deve ser opcional.

Quando o segundo parâmetro for definido como "vogais", a função deve
devolver o numero de vogais presentes na frase. Quando ele for definido
como "consoantes", a função deve devolver o número de consoantes
presentes na frase. Se este parâmetro não for passado para a função,
deve-se assumir o valor "vogais" para o parâmetro.


"""


def conta_letras(frase, contar='vogais'):
    vogais = ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U')
    contador = 0
    a = frase.split()
    b = ''
    for n in a:
        b = b + str(n)
    if contar == 'vogais':
        for x in b:
            if x in vogais:
                contador = contador + 1
            else:
                contador = contador
    if contar == 'consoantes':
        for x in b:
            if x not in vogais:
                contador = contador + 1
            else:
                contador = contador
    return contador





