from datetime import date

ano_nasc = int(input('Qual o ano de nscimento do atleta? '))
idade = date.today().year - ano_nasc
if idade <= 9:
    print('O atleta e da categoria mirin')
elif idade > 9 and idade <= 14:
    print('O atleta e da categoria infantil')
elif idade > 14 and idade <= 19:
    print('O atleta e da categoria junior')
elif idade == 20:
    print('O atleta e da categoria senior')
elif idade > 20:
    print('O atleta e da categoria master')
