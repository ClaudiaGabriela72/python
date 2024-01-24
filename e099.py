from time import sleep


def maior(* num):
    cont = mai = 0
    print(f'\nAnalisando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(0.5)
        if cont == 0:
            mai = valor
        else:
            if valor > mai:
                mai = valor
        cont += 1
        sleep(0.5)
    print(f'Foram informados {cont} valores ao todo.')
    sleep(0.5)
    print(f'E {mai} é o maior numero.')


maior(1, 4, 5, 6, 7, 9)
maior(9, 3, 1)
maior(1, 2)
maior(6)
maior()
