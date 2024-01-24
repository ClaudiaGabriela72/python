situa = dict()
situa['nome'] = str(input('Nome: '))
situa['media'] = float(input(f'Media de {situa["nome"]}:'))
for k, v in situa.items():
    print(f'{k} é igual a {v}')
if situa["media"] >= 6.0:
    print('Situação é igual a aprovado')
else:
    print('situação é igual a desaprovado')



