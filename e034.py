salario = float(input('Qual o seu salario '))
if salario >= 1250.00:
    novo = salario + (salario * 10) / 100
else:
    novo = salario + (salario * 15) / 100
print('Seu salario era de {}{:.2f}{} agora é {}'.format('\033[7;31;40m', salario, '\033[m', novo))
