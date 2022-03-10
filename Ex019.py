import random
'''a1 = input('Digite o nome do 1 aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do 3 aluno: ')
n4 = input('Digite o nome do quarto aluno: ')
r = random.randint(1, 4)
if r == 1:
    print('O aluno sorteado foi {}'.format(a1))
elif r == 2:
    print('O aluno escolhido foi {}'.format(n2))
elif r == 3:
    print('O aluno escolhido foi {}'.format(n3))
else:
    print('O aluno escolhido foi {}'.format(n4))'''
# Jeito do prof
a1 = str(input('Digite o nome do 1 aluno: '))
n2 = str(input('Digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do 3 aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))
lista = [a1, n2, n3, n4]
esc = random.choice(lista)
print('O escolhido foi {}'.format(esc))
