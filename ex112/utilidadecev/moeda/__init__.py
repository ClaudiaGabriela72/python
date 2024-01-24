def dobro(num, formt=False):
    dob = num * 2
    return dob if formt is False else moeda(dob)


def aumenta(num=0, taxa=0, formt=False):
    tot = num + (num * taxa/100)
    return tot if formt is False else moeda(tot)


def diminui(num=0, taxa=0, formt=False):
    tot = num - (num * taxa / 100)
    return tot if formt is False else moeda(tot)


def metade(num, formt=False):
    div = num / 2
    return div if formt is False else moeda(div)


def moeda(num, moeda='R$'):
    return f'{moeda}{num:0.2f}'.replace('.', ',')


def resumo(n=0, au=10, di=13):
    print('-' * 25)
    print(f'RESUMO DO PREÇO'.center(25))
    print('-' * 25)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'Aumentando {au}%: \t{aumenta(n, au, True)}')
    print(f'Diminuindo {di}%: \t{diminui(n, di, True)}')
