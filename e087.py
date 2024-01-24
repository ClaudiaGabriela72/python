pares = scol = mai = 0
matris = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matris[l][c] = int(input(f'Digite um valor para : [{l},{c}]'))
print('=-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matris [l][c]:^5}]', end='')
        if matris[l][c] % 2 == 0:
            pares = pares + matris[l][c]
    if matris[l][2]:
        scol = scol + matris[l][2]
    if matris[1][c] == mai:
        mai = matris[1][c]
    elif matris[1][c] > mai:
        mai = matris[1][c]
    print()
print('=-' * 30)
print(f'A soma de todos os valores pares é: {pares}')
print(f'A soma de todos os valores da terceira coluna é:{scol}')
print(f'O maior numero da segunda linha é {mai}')
