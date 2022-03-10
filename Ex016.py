import math
from decimal import Decimal
# jeito sem import
n = Decimal(input('Digite um numero real qualquer: '))
print('A parte inteira do numero e {}'.format(int(n)))
# Com import mostrando fatorial e o int
n2 = Decimal(input('Digite um numero real qualquer: '))
n2 = math.modf(n2)
print(n2)
# So mostrando o valor int do numero
n3 = Decimal(input('Digite um numero real qualquer: '))
n3 = math.trunc(n3)
print(n3)
