se = str(input('Sexo [M/F]: ')).strip().upper()
while se not in 'MmFf':
    se = str(input('invalido Digite novamente: '))
if se == 'M' or 'F':
    print('fim')

