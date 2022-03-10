num = input('Digite um numero de 0 a 9999: ')
c1 = len(num)
if c1 == 1:
    print('Unidade: ' + num[0])
elif c1 == 2:
    print('Unidade: ' + num[1])
    print('Dezena:  ' + num[0])
elif c1 == 3:
    print('Unidade: ' + num[2])
    print('Dezena:  ' + num[1])
    print('Centena: ' + num[0])
elif c1 == 4:
    print('Unidade: {}'.format(num[3]))
    print('Dezena:  {}'.format(num[2]))
    print('Centena: {}'.format(num[1]))
    print('Milhar:  {}'.format(num[0]))
else:
    print('Error: O numero digitado e grande demais.')
