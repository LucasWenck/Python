# Levando em consideracao uma faculdade que tenha peso 4 na 1 prova e peso 6 na 2, quanto seria a media de um aluno?
n1 = float(input('Informe a nota na prova 1: '))
n2 = float(input('Informe a nota da prova 2: '))
mf = (n1*4 + n2*6)/10
print('A media do aluno foi de {}'.format(mf))
if mf < 7:
    print('Infelizmente o aluno reprovou na materia.')
else:
    print('O aluno conseguiu passar na materia.')
