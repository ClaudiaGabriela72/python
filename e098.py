def contador(i, f, p):
    print(f'Contando de {i} ate {f} de {p} em {p} ')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            cont += p
        print('fim')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            cont -= p
        print('fim')


contador(1, 10, 1)
contador(10, 0, 2)
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
paso = int(input('Passo: '))
contador(inicio, fim, paso)
