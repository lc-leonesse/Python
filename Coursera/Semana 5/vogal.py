"""

Escreva a função vogal que recebe um único caractere como parâmetro e devolve True se ele for uma vogal e
False se for uma consoante.

Note que

vogal("a") deve devolver True

vogal("b") deve devolver False

vogal("E") deve devolver True

Os valores True e False devolvidos devem ser do tipo bool (booleanos)

Dica: Lembre-se que para passar uma vogal como parâmetro ela precisa ser um texto, ou seja, precisa estar entre aspas.

"""

def vogal(x):
    if x == "a" or x == "A":
        return True
    elif x == "e" or x == "E":
        return True
    elif x == "i" or x == "I":
        return True
    elif x == "o" or x == "O":
        return True
    elif x == "u" or x == "U":
        return True
    else:
        return False
