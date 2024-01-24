def leiaint(men):
    ok = False
    valor = 0
    while True:
        try:
            n = str(input(men))
            if n.isnumeric():
                valor = int(n)
                ok = True
            else:
                print('\033[0;31mErro! Digite um numero inteiro valido\033[m')
            if ok:
                return valor
        except ValueError:
            print('\033[0;31mErro! Digite apenas numeros.\033[m')


def leiafloat(men):
    valido = False
    while not valido:
        try:
            entrada = str(input(men)).replace(',', '.').strip()
            if entrada.isalpha() or entrada == '':
                print(f'\033[0;31mErro! "{entrada}" nao é um numero valido.\033[m')
            else:
                valido = True
                return float(entrada)
        except ValueError:
            print('\033[0;31mErro! digite um valor real valido.\033[m')


numi = leiafloat('Digite um numero Real: ')
numr = leiaint('Digite um numero Interio: ')
print(f'Voce digitou o numero  Inteiro {numi} e o numero real {numr}')

