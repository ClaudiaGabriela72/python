import random
a1 = str(input('escreva o nome do primeiro aluno '))
a2 = str(input('escreva o nome do segundo alno '))
a3 = str(input('escreva o nome do terceiro '))
a4 = str(input('escreva o nome do quarto '))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem dos alunos sera {}'.format(lista))
