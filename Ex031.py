distancia = float(input('Digite a distancia da viagem em kilometros: '))
if distancia <= 200:
    valor = 0.50 * distancia
    print('O valor de sua viagem vai ser R${:.2f}'.format(valor))
else:
    valor = 0.45 * distancia
    print('O valor de sua longa vaigem vai ser R${:.2f}'.format(valor))
