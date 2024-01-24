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


def resumo(n, au, di):
    print('-' * 25)
    print(f'     RESUMO DO PREÇO   ')
    print('-' * 25)
    print(f'Preço analisado:', ' '*8, n)
    print(f'Dobro do preço:', ' '*8, dobro(n))
    print(f'Metade do preço:', ' '*8, metade(n))
    print(f'Aumentando {au}%:', ' '*8, aumenta(n))
    print(f'Diminuindo {di}%:', ' '*8, diminui(n))
