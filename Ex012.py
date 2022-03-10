# Liquida de 5% em tudo
n1 = float(input('Informe o valor do produto: R$'))
print('O valor do produto, em liquidacao, vale {}'.format(n1*(95/100)))
# Outro jeito de fazer
prec = float(input('Digite o preco do produto: R$'))
precn = prec - (prec * 5/100)
print('O produto que custava {:.2f}, na liquida de 5% custa {:.2f}'.format(prec, precn))
