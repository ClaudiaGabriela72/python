def voto(ano, nas):
    ano = 2023
    cal = ano - nas
    print(f'Com {cal} anos: ', end='')
    if cal >= 68:
        return print('O voto é opcional')
    if cal >= 18:
        return print('O voto é obrigatorio')
    else:
        return print('O voto é negado')



ano = 2023
nas = int(input('O ano do seu nascimento? '))
voto(ano, nas)
