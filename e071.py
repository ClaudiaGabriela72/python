print('=' * 20)
print('{:^30}'.format('BANCO CEV'))
print('=' * 20)
notacin = 0
notadez = 0
notavin = 0
notaum = 0
valor = int(input('Qual valor voce quer sacar? '))
while True:
    if valor >= 50:
        valor = valor - 50
        notacin += 1
    if valor == 0:
        break
    elif valor >= 20:
        valor = valor - 20
        notavin += 1
        if valor == 0:
            break
    elif valor >= 10:
        valor = valor - 10
        notadez += 1
        if valor == 0:
            break
    elif valor >= 1:
        valor -= 1
        notaum += 1
print(f'Foram {notacin} notas de 50R$')
print(f'Foram {notavin} notas  de 20R$')
print(f'Foram {notadez} notas  de 10R$')
print(f'Foram {notaum} notas de 1R$')
