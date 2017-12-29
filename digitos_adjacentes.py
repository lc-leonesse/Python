"""

Dizer se um número informado pelo usuário possui 2 ou mais dígitos adjacentes iguais


"""

x = int(input("Digite um número inteiro: "))

da = False
anterior = x % 10
x = x // 10
pos = 0

while x > 0 and not da:
    posterior = x % 10
    if posterior == anterior:
        da = True
    else:
        pos = pos + 1
        anterior = posterior
        x = x //10

if da:
    print("sim")
else:
    print("não")




