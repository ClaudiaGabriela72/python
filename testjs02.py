num = []
res = 'sim'
while res != 'nao':
    tem = input('Digite um numero de 1 a 100: ')
    res = input('Quer continuar ? ')
    num += tem

soma = sum(num)
print(f'Você digitou {len(num)} numeros')
print(f'O maior numero digitado foi {max(num)}')
print(f'O menor numero informado foi {min(num)}')
print(f'A soma de todos os numeros foi {soma}')
