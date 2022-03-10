r1 = float(input('Digite o valor da reta 1: '))
r2 = float(input('Digite o valor da reta 2: '))
r3 = float(input('Digite o valor da reta 3: '))
# O if se baseia nas regras de existencia de um triangulo em que a soma de dois lados precisa ser maior que o lado
# restante.
if r2 + r3 > r1 and r1 + r3 > r2 and r1 + r2 > r3:
    print('As retas informadas conseguem criar um triangulo.')
else:
    print('As retas informadas nao conseguem criar um triangulo.')
