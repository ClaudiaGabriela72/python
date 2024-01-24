jogador = dict()
time = list()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
    partidas.clear()
    for g in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {g}? ')))
        jogador['gols'] = partidas[:]
        jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    res = input('Quer continuar[S/N] ? ').upper()[0]
    if res == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não existe jogador com codgo {busca}')
    else:
        print(f'--- Levantamento do Jogador {time[busca] ["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
    print('-' * 40)
