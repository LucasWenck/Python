# Considerando que 1 litro de tinta pinta 2m quadrados
lar = float(input('Informe a largura(em metros) da parede: '))
alt = float(input('Informe a altura(em metros) da parede: '))
print('A area da parede é {}m²\nE é necessario {:.2f} litros de tinta para pintar a parede.'
      .format(lar*alt, lar*alt/2))
