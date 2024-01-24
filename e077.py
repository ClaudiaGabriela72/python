
palavra = ('APRENDER', 'CURSO', 'ESTUDAR', 'TRABLHAR', 'CRIAR', 'PYTHON')
for c in palavra:
    print(f'\nNa palavra {c} temos',end=' ')
    for letra in c:
        if letra in 'AEIOU':
            print(f'{letra}',end=' ')