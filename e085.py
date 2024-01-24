num = [[], []]
valor = 0
for p in range(0, 7):
    valor = int(input(f'Digite o {p}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    if valor % 2 != 0:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(num)
print(f'Os pares são {num[0]}')
print(f'Os impares são {num[1]}')
