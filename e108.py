from utilidades import moeda

n = float(input('Digite um preço: '))
print(f'A metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}')
print(f'O dobrode {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}')
print(f'Aumentando 10% de {moeda.moeda(n)} é {moeda.moeda(moeda.aumenta(n))}')
print(f'Diminuindo 13% de {moeda.moeda(n)} é {moeda.moeda(moeda.deminui(n))}')
