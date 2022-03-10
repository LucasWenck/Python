menu_opt = int(input('1 - para usar o convertidor\n0 - para sair\n'))
while menu_opt == 1:
    num = int(input('Qual o numero que voce deseja converter? '))
    opt = int(input(('Em que base voce quer converter o numero?\n1 - Binario\n2 - Octal\n3 - Hexadecimal\n')))
    if opt == 1:
        print('O numero {} em binario fica {}'.format(num, bin(num).replace('0b', '')))
    elif opt == 2:
        print('O numero {} em octal fica {}'.format(num, oct(num).replace('0o', '')))
    elif opt == 3:
        print('O numero {} em hexadecimal fica {}'.format(num, hex(num).replace('0x', '')))
    menu_opt = int(input('1 - para fazer outra conversao\n0 - Para sair\n'))
print('Obrigado por usar o nosso convertidor')
