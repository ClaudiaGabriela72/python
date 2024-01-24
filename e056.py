idadem = 0
cont = 0
maior = 0
menor = 0
for c in range(1, 5):
    print('-' * 10, '{} PESSOA '.format(c), '-' * 10)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    if sexo == 'M':
        if idade > maior:
            maior = idade
        if idade < menor:
            menor = idade
            print('O homem mais felho é {} e tem {} anos'.format(nome, idade))
    if sexo == 'F':
        cont = cont + 1
        if idade > maior:
            maior = idade
            idadem = maior
        if idade < menor:
            menor = idade
print('tem {} mulheres e a mais velha tem  {} anos'.format(cont, idadem))
m = idade / 4
print('A media de idade do grupo é de {}'.format(m))
print('O homem mais felho é {} e tem {} anos'.format(nome, idade))
