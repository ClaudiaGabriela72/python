print('='*25)
print('\033[1;31m10 PRIMEIROS TERMOS\033[m')
print('='*25)

pri = int(input('Primeiro termo: '))
ra = int(input('Razão: '))
dec = pri + (10 - 1) * ra

for c in range(pri, dec + ra, ra):
    print(c, end='-')
