print('-' * 30)
print(f'{"LISTA DE PREÇO":^30}')
print('-' * 30)
tuple = ('Lapis', 1.75,
         'Caneta', 2.0,
         'Caderno', 9.55,
         'Estojo', 12,
         'Compasso', 3.76,
         'Mochila', 55.0)

for pos in range(0, len(tuple)):
    if pos % 2 == 0:
        print(f'{tuple[pos]:.<30}',end=' ')
    else:
        print(f'R$ {tuple[pos]:.2f}')
