from ex115.lib.interface import *

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoas', 'sair do sistema'])
    if resposta == 1:
        print('Opiçao 1')
    elif resposta == 2:
        print('Opiçao 2')
    elif resposta == 3:
        print('Saindo do menu')
        break
    else:
        print('Erro! Digite uma opção valida.')
