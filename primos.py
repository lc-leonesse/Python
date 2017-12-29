"""

Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve o maior número
primo menor ou igual ao número passado à função

Note que

maior_primo(100) deve devolver 97

maior_primo(7) deve devolver 7

Dica: escreva uma função éPrimo(k) e faça um laço percorrendo os números até o número dado checando se o número é
primo ou não; se for, guarde numa variável. Ao fim do laço, o valor armazenado na variável é o maior primo encontrado.

"""



def ePrimo(n):
    divisores = 0
    i = 1

    while i <= n:
        if n % i == 0:
            divisores = divisores + 1
        i = i + 1
    if divisores == 2:
        return True
    else:
        return False

def maior_primo(n):
    x = 1
    y = 1
    while x <= n:
        if ePrimo(x) == True:
            y = x
            x = x + 1
        else:
            x = x + 1
    return y




                
            
           

        





    
    
        








