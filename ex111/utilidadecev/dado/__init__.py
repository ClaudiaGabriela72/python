def leiadinheiro(men):
    valido = False
    while not valido:
        entrada = str(input(men)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mErro! "{entrada}" nao é um numero valido.\033[m')
        else:
            valido = True
            return float(entrada)

