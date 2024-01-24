cont = ('zero', 'um', 'dois', 'tres', 'quadro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'Dez')

while True:
    num = int(input('Digite um numero de 0 a 10: '))
    if 0 < num <= 20:
        break
        print('digite novamente', end=' ')
print(f'você digitou o numero  {cont[num]} ')
