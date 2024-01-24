print('-'*8, 'Seguencia de fibonacci', '-'*8)
num = int(input('Digite o numero de termos que deseja: '))
t1 = 0
t2 = 1
c = 0
print('{}-{}'.format(t1, t2), end='-')
while c != num:
    c += 1
    t3 = t1 + t2
    print(t3, end='-')
    t1 = t2
    t2 = t3
print('fim')