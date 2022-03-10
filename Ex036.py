casa_valor = float(input('Informe o valor da casa: R$'))
entrada_comprador = float(input('Com quanto o comprador vai entrar na proposta? R$'))
casa_valor_ent = casa_valor - entrada_comprador
salario = float(input('Informe o salario do comprador: R$'))
tempo = float(input('Em quantos anos o comprador vai quitar a casa? '))
tempo_mensal = tempo * 12
prest_mensal = casa_valor_ent/tempo_mensal
if prest_mensal > 0.3 * salario:
    print('Emprestimo negado, o valor da prestacao e muito alto para este salario.')
else:
    print('O valor de R${:.2f} sera cobrado mensalmente ate que o pagamento seja completo, tenha um bom dia!'.format(prest_mensal))
