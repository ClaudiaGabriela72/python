from utilidades import moeda

n = float(input('Digite um preço: '))
print(f'A metade de {moeda.moeda(n)} é {moeda.metade(n, False)}')
print(f'O dobrode {moeda.moeda(n)} é {moeda.dobro(n)}')
print(f'Aumentando 10% de {moeda.moeda(n)} é {moeda.aumenta(n, 10)}')
print(f'Diminuindo 13% de {moeda.moeda(n)} é {moeda.deminui(n, 13)}')
