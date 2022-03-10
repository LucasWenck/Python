n1 = int(input('Qual numero voce quer a tabuada? '))
d = 1
while d <= 10:
    print('-' * 12)
    print('{} x {:^2} = {}'.format(n1, d, n1*d))
    d = d + 1
    if d > 10:
        print('Gostou do resultado? deixa seu joinha!')
        break
