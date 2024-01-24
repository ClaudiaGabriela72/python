valores = []
cont = 's'
while cont in 'sS':
    num = (int(input('Digite um valor: ')))
    cont = str(input('Quer continuar [S/N] ? '))
    if num not in valores:
        valores.append(num)
        print('Adicionado com sucesso')
    else:
        print('erro, esse numero ja foi adicionado')
valores.sort()
print(f'voce digitou os valores {valores} e {num}')
