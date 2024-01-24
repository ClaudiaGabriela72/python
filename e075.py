tupla = (int(input('Digite um numero:')),
         int(input('Digite mais um numero: ')),
         int(input('Digite mais um numero: ')),
         int(input('Digite o ultimo numero: ')))
print(f'Voce digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)}')
print(f'O numero 3 aparece primeiro na posição {tupla.index(3)}')
print('sao pares os valores', end=' ')
for n in tupla:
    if n % 2 == 0:
     print(f' {n}', end=' ')
