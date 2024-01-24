valor = []
impar = []
pares = []
while True:
    valor.append(int(input('Digite um numero: ')))
    quer = str(input('Quer continuar? '))
    if quer in 'Nn':
        break
for i, v in enumerate(valor):
    if v % 2 == 0:
        pares.append(v)
    else:
        impar.append(v)
print(f'A lista de impares é {impar}')
print(f'A lista de pares é {pares}')
print(f'A lista completa é {valor}')
