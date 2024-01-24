valor = []
cont = 0
while True:
    valor.append(int(input('Digite um valor: ')))
    quer = str(input('Quer continuar [S/N]? '))
    cont += 1
    if quer in 'Nn':
        break
valor.sort(reverse=True)
#n = valor.count(5)
if 5 in valor:
    print(f'O valor 5 pertence a essa lista!')
else:
    print('O valor 5 não pertrnce a essa lista')
print(f'Voce digitou {cont} elementos.')
print(f'Os valores em ordem decresente são {valor}')


