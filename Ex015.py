from decimal import Decimal


d = Decimal(input('Por quantos dias o carro foi alugado? '))
if d >= 10:
    print('Parabens por ter alugado o carro por pelo menos 10 dias, voce ganhou um desconto dos kilometros rodados!!')
    pd = d * 60
    print('O consumidor so deve pagar R${:.2f} devido a seu desconto especial.'.format(pd))
else:
    k = Decimal(input('Quantos Km o carro percorreu? '))
    pd = d * 60
    pk = k * 0.15
    pt = pd + pk
    print('O consumidor deve pagar R${:.2f}.'.format(pt))
    print('R${:.2f} sao pelos dias alugados.'.format(pd))
    print('R${:.2f} sao pelos kilometros rodados.'.format(pk))
