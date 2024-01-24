c = ['\033[m',#0 sem cor
'\033[0;30;41m'#1 vermelho
 ]


def titulo(men, cor=0):
    tam = len(men) + 4
    print(c[cor], end='')
    print('¨' * tam)
    print(f'  {men}')
    print('¨' * tam)
    print(c[0], end='')


while True:
    titulo('SISTEMA DE AJUDA PYHELP', 1)
    comando = input('Qual funçao deseja saber?[fim para parar]. ')
    help(comando)
    if comando.upper() in 'FIM':
        break
titulo('ATE LOGO', 1)
