from ex109 import moeda
n = float(input('Digite um valor: '))
print(f'O dobro de {moeda.moeda(n)} é {moeda.dobro(n, True)}')
print(f'A metade de {moeda.moeda(n)} é {moeda.metade(n, True)}')
print(f'Aumentando 10% é {moeda.aumenta(n, 10, True)}')
print(f'Diminuindo 13% é {moeda.diminui(n, 13, True)} ')
