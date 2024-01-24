def fatorial(num=1, show=False):
    """
    fatorial(num=1,show=False)
    :param num: O numero a ser calculado
    :param show: (Opcional) mostra ou nao a conta
    :return: retorna o fatorial de um numero n.
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show == True:
            print(f'{c} x ', end='')
            return print(f'= {f}')
    return print(f)


help(fatorial())
# n = int(input('Digite um numero: '))
# print(fatorial(n, show=False))

#help(fatorial())
