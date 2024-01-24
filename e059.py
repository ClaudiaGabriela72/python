n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
escolha = 0
while escolha != 5:
    print("""    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMEROS
    [5] SAIR DO PROGRAMA """)
    escolha = int(input(('Qual sua oopção: ')))
    if escolha == 1:
        soma = n1 + n2
        print('A soma é {}'.format(soma))
    elif escolha == 2:
        mul = n1 * n2
        print('A multiplicação é {}'.format(mul))
    elif escolha == 3:
        if n1 > n2:
            print('O 1  numero  que é o {} é o maior'.format(n1))
        else:
            print('O 2 numero que é o {} é o maior '.format(n2))
    elif escolha == 4:
      print('Informe os novos numeros')
      n1 = int(input('Primeiro valor: '))
      n2 = int(input('Segundo valor '))
    elif escolha == 5:
        print('Finalizando...')
    else:
        print('Opção invalida, Tentemais uma vez.')
print('fim')

