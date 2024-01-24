maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Qual é o peso {} pessoa?'.format(c)))
    if c == 1:
        menor = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi de {}Kg'.format(maior))
print('O menor peso foi de {}Kg'.format(menor))
