def opçoes(op):
    while True:
        print('-' * 30)
        print('MENU PRINCIPAL'.center(30))
        print('-' * 30)
        print('\033[0;49;32m1 - Ver pessoas cadastradas\033[m')
        print('\033[0;49;33m2 - Cadastra nova pessoa\033[m')
        print('\033[0;49;34m3 - Sair do sistema\033[m')
        print('-' * 30)
        try:
            op = int(input('\033[0;49;93mQual sua opçao:\033[m '))
            if op == 1:
                print('opeçao 1')
            elif op == 2:
                print('opeçao 2')
            elif op == 3:
                print('opeçao 3')
                break
            else:
                print('\033[0;49;31mOpçao invalida.\033[m')
        except:
            print('\033[0;49;31mErro! digite um numero valido.\033[m')


opçoes('Qual sua opçao: ')