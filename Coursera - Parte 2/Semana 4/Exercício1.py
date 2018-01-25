"""

Faça um programa que receba obrigatoriamente 3 números em ordem
crescente(fazer a verificação) e um quarto numero que não siga essa
regra. Mostre em seguida os quatro números em ordem decrescente.
Suponha que o usuário digitará 4 números diferentes

"""

a = int(input('Informe o primeiro número: '))
b = int(input('Informe o segundo número: '))
if b < a:
    print('O segundo número precisa ser maior que o primeiro número')
    b = int(input('Informe o segundo número: '))

c = int(input('Informe o terceiro número: '))

if c < b:
    print('O terceiro número precisa ser maior que o segundo número')
    c = int(input('Informe o terceiro número: '))

d = int(input('informe o quarto número: '))

x = [a, b, c, d]

x.sort(reverse=True)

print(x)

