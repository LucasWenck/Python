from datetime import date
ano = int(input('Informe ano (ou digite 0 para usar o ano atual do computador): '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0:
    print('O ano {} e bissexto.'.format(ano))
elif ano % 100 == 0 and ano % 400 == 0:
    print('O ano {} e bissexto.'.format(ano))
else:
    print('O ano {} nao e bissexto.'.format(ano))
