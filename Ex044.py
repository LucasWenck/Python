preco = float(input('Qual o preco do produto? R$'))
forma_pagamento = int(input('Qual sera a forma de pagamento?\n1 - A vista\n2 - A vista no cartao\n3 - Ate 2x no cartao\n4 - 3x ou mais no cartao\n'))
if forma_pagamento == 1:
    print('O valo a ser pagado sera R${:.2f}'.format(preco * 0.9))
elif forma_pagamento == 2:
    print('O valor a ser pagado sera R${:.2f}'.format(preco * 0.95))
elif forma_pagamento == 3:
    print('O valor a ser pagado sera R${:.2f}'.format(preco))
elif forma_pagamento == 4:
    print('O valor a ser pagado sera R${:.2f}'.format(preco * 1.2))
else:
    print('Opcao invalida')
