valores = list()
maior = 0
menor = 0
for c in range(0, 5):
    valores.append(int((input(f'Digite um valor na posiçao {c}: '))))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print(f'Voce digitou os valores {valores}')
print(f'O menor numero digitado foi {menor} na posiçao',end=' ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end=' ')
print(f'\nO maior numero digitado foi {maior} na posiçao', end= ' ')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end=' ')