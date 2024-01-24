from random import randint
from time import sleep
numero = list()
listp = list()


def sorteia(lista):
    print('Sorteando 5 valores:', end=' ')
    for c in range(0, 5):
        num = randint(0, 9)
        lista.append(num)
        print(num, end=' ')
        sleep(1)
    print('Pronto')


def somap(lista):
    par = 0
    for q in lista:
        if q % 2 == 0:
            par += q
    print(f'Somando todos os valores pares de {lista} a soma é {par}')


sorteia(numero)
somap(numero)
