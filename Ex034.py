salario = float(input('Digite o valor do salario para calculo do aumento: R$'))
if salario > 1250.00:
    print('O valor de seu novo salario é R${:.2f}'.format(salario*110/100))
else:
    print('O valor de seu novo salario é R${:.2f}'.format(salario*115/100))
