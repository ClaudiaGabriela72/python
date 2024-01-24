dias = int(input('Quantos dias se passaram ? '))
km = float(input('Quantos kilometros foi rodado ? '))
pago = (dias * 60) + (km * 0.15)
print('o valor do aluguel é de {:.2f}'.format(pago))
