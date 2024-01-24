import moeda
n = float(input('Digite um valor: '))
print(f'O dobro de {moeda.moeda(n)} é {moeda.dobro(n)}')
print(f'A metade de {moeda.moeda(n)} é {moeda.metade(n)}')
print(f'Aumentando 10% é {moeda.aumenta(n, 10)}')
print(f'Diminuindo 13% é {moeda.diminui(n, 13)} ')
