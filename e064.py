n = int(input('Digite um numero [999 para parar]:'))
cont = 0
soma = 0
while n != 999:
    soma += n
    n = int(input('Digite um numero [999 para parar]:'))
    cont += 1
print('Voce digitou {} e a soma deles é {}'.format(cont, soma))
