from random import randint
print('Eu pensei em um numero entre 0 a 10, tente adivinhar, voce tem apenas uma tentativa ')
nu = input('Digite o numero  ')
nus = randint(0, 10)
if nu == nus:
    print('voce acertou')
else:
    print('voce errou')
print('o numero era {}'.format(nus))
