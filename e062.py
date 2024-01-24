print('='*25)
print('\033[1;31m10 PRIMEIROS TERMOS\033[m')
print('='*25)
pri = int(input('Primeiro termo: '))
ra = int(input('Razão: '))
ter = pri
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        ter += ra
        c += 1
        print('{}'.format(ter), end='-')
    print('pausa')
    mais = int(input('Quantos termos voce quer a mais? '))
print('fim')