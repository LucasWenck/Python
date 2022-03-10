nota_av1 = float(input('Qual foi a nota na Av1? '))
nota_av2 = float(input('Qual doi a nota na Av2? '))
media = (nota_av1 + nota_av2)/2
if media < 5:
    print('Reprovado')
elif media >= 5 and media < 7:
    print('Recuperacao')
else:
    print('Aprovado') 
