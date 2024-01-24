from utilidades import moeda

n = float(input('Digite um valor: '))
print(f'O dobro de {n} é {moeda.dobro(n)}')
print(f'A metade de {n} é {moeda.metade(n)}')
print(f'Aumentando 10% é {moeda.aumenta(n, 10)}')
print(f'Diminuindo 13% é {moeda.deminui(n, 13)} ')
