"""
1038
Com base na tabela abaixo, escreva um programa que leia o código de
um item e a quantidade deste item. A seguir, calcule e mostre o valor
da conta a pagar.



Entrada

O arquivo de entrada contém dois valores inteiros correspondentes ao
código e à quantidade de um item conforme tabela acima.

Saída

O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo
valor a ser pago, com 2 casas após o ponto decimal.



"""


valor = input()

separado = valor.split(' ')
codigo = int(separado[0])
quantidade = int(separado[1])


if codigo == 1:
    preco = 4.00
elif codigo == 2:
    preco = 4.50
elif codigo == 3:
    preco = 5.00
elif codigo == 4:
    preco = 2.00
elif codigo == 5:
    preco = 1.50

total = preco * quantidade

print('Total: R$ ', '{0:,.2f}'.format(total))





