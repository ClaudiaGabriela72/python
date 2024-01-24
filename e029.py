ve = int(input('Qual era a velocidade do carro? '))
if ve > 80:
    print('Voce foi multado')
    mul = (ve - 80) * 7
    print('A multa sera de {}R$'.format(mul))
else:
    print('voce nao foi multado')
