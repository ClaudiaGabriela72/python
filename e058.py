from random import randint
nus = randint(0, 1)
acertou = False
print('Eu pensei em um numero entre 0 a 10, tente adivinhar.')
palpite = 0
while not acertou:
    nu = input('Qual o seu palpite? ')
    palpite += 1
    if nu == nus:
        acertou = True
        print('voce acertou')
print('o numero era {} voce levou {} tentativas para acertar'.format(nus, palpite))
