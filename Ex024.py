cid = input('Digite o nome de sua cidade: ')
cid = cid.strip()
cid = cid.upper()
cid = cid.split()
cid1 = 'SANTO' in cid
print('O primeiro nome e santo? ', cid1)
# Jeito 2
if cid[0] == 'SANTO':
    print('Sua cidade comeca com santo')
else:
    print('Sua cidade nao comeca com santo')
