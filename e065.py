quer = str(input('vamos começar? (sim/nao) ')).upper()[0]
cont = 0
soma = 0
maior = 0
menor = 0
while quer == 'S':
    cont += 1
    num = int(input('Digite um numero:'))
    quer = str(input('Quer continuar? ')).upper()[0]
    soma += num
    med = soma / cont
    if num > maior:
        maior = num
    if num < maior:
        menor = num
print('A media de {} numeros é {:.2f}'.format(cont, med))
print('O menor numero digitado é {} e o maior é {}.'.format(menor, maior))
