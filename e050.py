soma = 0
for c in range(6):
    n = int(input('Digite um numero: '))
    #soma = soma + n
    if n % 2 == 0:
        soma = soma + n
print('a soma de todos os numeros é {}'.format(soma))
