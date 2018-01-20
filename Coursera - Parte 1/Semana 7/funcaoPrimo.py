"""

Informar se o número que o usuário está digitando é primo ou não

"""


def primo(n):
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

n = int(input("Digite um número inteiro: "))

while n > 0:
    if primo(n) == True:
        print(n,"é primo!")
    else:
        print(n,"não é primo!")
    n = int(input("Digite um número inteiro: "))