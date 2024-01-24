num1 = int(input('Digite o primeiro numero '))
num2 = int(input('Digite o segundo numero '))
if num1 > num2:
    print('O primeiro numero \033[31m{}\033[m é maior que o segundo \033[33m{}'.format(num1, num2))
elif num2 > num1:
    print('O segundo numero \033[34m{}\033[m é maior que o primeiro \033[35m{}'.format(num2, num1))
else:
    print('\033[30mOs numeros sao iguais')
