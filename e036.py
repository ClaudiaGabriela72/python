vcasa = float(input('Qual o valor da casa que voce gostaria de comprar? '))
salario = float(input('Qual o valor do seu salario? '))
ano = int(input('Com quantos anos voce pretende pagar? '))
pres = (vcasa / ano)/12
mini = salario * 30 /100
if pres <= mini:
    print('\033[31mSeu financeamento foi negado\033[m')
else:
    print('\033[33mSeu financeamento foi aprovado\033[m')
