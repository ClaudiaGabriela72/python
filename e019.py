from random import choice
a1 = str(input('escreva o nome do primeiro aluno '))
a2 = str(input('escreva o nome do segundo alno '))
a3 = str(input('escreva o nome do terceiro '))
a4 = str(input('escreva o nome do quarto '))
lista = [a1, a2, a3, a4]
ale = choice(lista)
print('O a luno que foi escolhido é o {}'.format(ale))
