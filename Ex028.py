from random import randint
num = randint(0, 5)
guess = int(input('O computador pensou em um numero de 0 a 5, qual numero vc acha que ele escolheu? '))
if guess == num:
    print('Uau, voce acertou!!')
else:
    print('Errou otario! Eu pensei no numero {}'.format(num))
