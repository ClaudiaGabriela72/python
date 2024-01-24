vi = int(input('Qual é a distancia de sua viagem (km) ? '))
if vi <= 200:
    re = vi * 0.50
else:
    re = vi * 0.45
print("sua viagem custara {}R$".format(re))

