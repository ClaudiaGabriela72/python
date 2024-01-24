nota1 = float(input('Qual é sua nota de artes? '))
nota2 = float(input('Qual sua nota de matematica? '))
med = (nota1 + nota2)/2
if 7 > med >= 5.0:
    print('\033[31mVoce foi reprovado')

elif med >= 5.0:
    print('\033[32mVoce esta de recuperaçao')

elif med >= 7.0:
    print('\033[34mVoce passou! Parabens.')

