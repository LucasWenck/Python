import math
cato = float(input('Informe o cateto oposto: '))
cata = float(input('Informe o cateto adjacente: '))
hyp = math.hypot(cato, cata)
print('A hypotenusa de seu triangulu equivale a {}'.format(hyp))
