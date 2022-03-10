from datetime import date

ano_nasc = int(input('Informe o ano de nascimento da pessoa: '))
if date.today().year - ano_nasc < 18:
    print('Ainda nao precisa se alistar. Faltam {} anos para voce se alistar cara.'.format(18 - (date.today().year - ano_nasc)))
elif date.today().year - ano_nasc == 18:
    print('E hora de se alistar.')
elif date.today().year - ano_nasc > 18:
    print('Ja passou a hora de se alistar, se voce ainda nao se alistou, voce esta atrasado em {} anos'.format((date.today().year - ano_nasc) - 18))
