
num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[32m',end=' ')
        tot += 1
    else:
        print('\033[34m', end=' ')
    print(c, end=' ')
print('\n\033[mo número {} foi divisivel {} vezes'.format(num, tot), end=' ')
if tot == 2:
    print('\nEle é primo.')
