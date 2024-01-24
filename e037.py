
numero = int(input('Digite um numero '))
print('Qual a base que voce desja? ')
print("""1-Binario-H
2-octal
3-hexadecimal""")
nums = int(input('escolha uma opçao: '))

if nums == 3:

    print('o numero em hexadecimal {}'.format(hex(numero)[2:]))

elif nums == 1:
    print('O numero {} em binario é {}'.format(numero, bin(numero)[2:]))

elif nums == 2:
    print('O numero {} em octal é {}'.format(numero, oct(numero)))

else:
    print('Opçao invalida')
