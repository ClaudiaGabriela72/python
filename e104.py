def leiaint(men):
    ok = False
    valor = 0
    while True:
        n = str(input(men))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro ! Digite um numero inteiro valido\033[m')
        if ok:
            return valor


n = leiaint('Digite um numero:')
print(f'Voce digitou o numero {n}')
