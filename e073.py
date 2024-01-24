from random import randint
tupla = (randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5))
print(f'Os valores sorteados foram', end=' ')
for con in tupla:
    print(con, end=' ')

print(f'\nO maior numero foi {max(tupla)}\n e o menor foi {min(tupla)}')

