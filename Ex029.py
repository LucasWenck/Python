from decimal import Decimal
velocidade = Decimal(input('Em quantos K/h o motorista passou na regiao? '))
if velocidade <= 80:
    pass
else:
    multa = 7 * (velocidade - 80)
    print('O motorista recebu uma multa no valor de R${:.2f}'.format(multa))
