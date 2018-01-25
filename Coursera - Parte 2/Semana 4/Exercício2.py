"""

Faça um programa que leia a hora inicial de uma partida de tênis
(a hora é composta por duas variáveis inteiras: hora e minuto), a
duração da partida (em horas e minutos) e mostre que horas a
partida terminou

"""

a = int(input('Informe a hora de início da partida: '))
if a > 23 and a < 0:
    print('Informe uma hora válida (de 0h até 23h')
    a = int(input('Informe a hora de início da partida: '))
b = int(input('Informe os minutos de início da partida: '))
if b > 59 and b < 0:
    print('Informe uma quantidade de minutos válida (de 0 até 59)')
    b = int(input('Informe os minutos de início da partida: '))
c = int(input('Informe a quantidade de horas de duração partida: '))
d = int(input('Informe a quantidade de minutos de duração da partida: '))
if d > 59 and d < 0:
    print('Informe uma quantidade de minutos válida (de 0 até 59)')
    d = int(input('Informe a quantidade de minutos de duração da partida: '))

x = a + c
y = b + d

while y >= 60:
    z = y // 60
    w = y % 60
    y = w
    x = x + z


print('A partida terminou às ', x, ' horas e', y, ' minutos')

