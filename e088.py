from random import randint
import time
print('-' * 30)
print('     JOGO DA MEGA SENA      ')
print('-' * 30)
jogo = int(input('Quantos jogos você quer? '))
print('=-' * 3, f'SORTEANDO {jogo} JOGOS', '=-' * 3)
sor = []
for p in range(1, jogo + 1):
    sor = [randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60)].sort()
    print(f'Jogo {p}:{sor}', time.sleep(1))
