print('='*25)
print('\033[1;31m10 PRIMEIROS TERMOS\033[m')
print('='*25)
pri = int(input('Primeiro termo: '))
ra = int(input('Razão: '))
ter = pri
c = 1
while c <= 10:
    ter += ra
    c += 1
    print('{}'.format(ter), end='-')
print('fim')
