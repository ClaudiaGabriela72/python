from random import randint
from time import sleep
from operator import itemgetter
maior = menor = 0
dic = dict()
lista = list()
for e in range(1, 5):
    dic['jogador'] = randint(0, 6)
    for v in dic.values():
        lista.append(v)
        print(f'O jogador{e} tirou {v}')
        sleep(1)
rank = dict(lista)

print(lista, rank)


