cont = 0
cot = 0
for c in range(1, 8):
    ano = int(input('Digite o ano da {} pessoa: '.format(c)))

    if ano <= 2004:
        cont += 1

    if ano > 2005:
        cot += 1

print("Ao todo tivemos {} pessoas maiores de idade".format(cont))
print('Ao todo tivemos {} pessoas menores de idade'.format(cot))
