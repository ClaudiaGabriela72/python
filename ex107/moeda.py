def dobro(num, moeda=True):
    dob = num * 2
    if moeda == True:
        return (f'{dob}R$')
    else:
        return dob


def aumenta(num, taxa, moeda=True):
    tot = num + (num * taxa/100)
    if moeda == True:
        return (f'{tot}R$')
    else:
        return tot


def diminui(num, taxa, moeda=True):
    tot = num - (num * taxa / 100)
    if moeda == True:
        return (f'{tot}R$')
    else:
        return tot


def metade(num, moeda=True):
    div = num / 2
    if moeda == True:
        return (f'{div}R$')
    else:
        return div


def moeda(num):
    return (f'{num}R$')


def resumo(n, au, di):
    print('-' * 25)
    print(f'     RESUMO DO PREÇO   ')
    print('-' * 25)
    print(f'Preço analisado:', ' '*8, n)
    print(f'Dobro do preço:', ' '*8, dobro(n))
    print(f'Metade do preço:', ' '*8, metade(n))
    print(f'Aumentando {au}%:', ' '*8, aumenta(n))
    print(f'Diminuindo {di}%:', ' '*8, diminui(n))
