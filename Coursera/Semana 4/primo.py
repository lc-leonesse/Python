"""

Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo. Se o número for primo,
imprima "primo". Caso contrário, imprima "não primo".

"""

n = int(input("Digite um número inteiro: "))

divisores = 0
i = 1

while i <= n:
    if n % i == 0:
        divisores = divisores + 1
    i = i + 1
if divisores == 2:
    print("primo")
else:
    print("não primo")


