"""

Somar os algarismos de um número informado pelo usuário

"""

x = int(input("Digite um número inteiro: "))

soma = 0

while x != 0:
    resto = x % 10
    x = (x - resto)//10
    soma = soma + resto

print(soma)
