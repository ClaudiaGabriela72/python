dic = dict()
total = 0
cont = 0
dic['nome'] = str(input('Nome do jogador: '))
list = []
partidas = int(input(f'Quantas partidas {dic["nome"]} jogou? '))
for e in range(0, partidas):
    dic['gols'] = int(input(f'Quantos gols na {e} ? '))
    list.append(dic['gols'])
    dic['gols'] = list
for g in list:
    total += g
    dic['Total'] = total
for i in range(0, partidas):
    cont = g
    print(f'Na partidada {i} ele fez {g} gols')
print(dic)
for k, v in dic.items():
    print(f'O campo {k} tem valor {v}')

