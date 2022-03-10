import math
a = int(input('Informe o angulo em graus: '))
ar = math.radians(a)
aS = math.sin(ar)
aC = math.cos(ar)
aT = math.tan(ar)
print('O seno do angulo e {}\nO coseno do angulo e {}\nA tangente do angulo e {}'.format(aS, aC, aT))
