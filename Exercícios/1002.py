from decimal import Decimal, getcontext

raio = Decimal(input())
pi = Decimal(3.14159)

A = Decimal(pi * (raio ** 2))



print('A=%f' % round(A,4))

