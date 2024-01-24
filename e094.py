lista = list()
dic = dict()
pessoas = med = soma = mulher = cont = 0
while True:
    pessoas += 1
    dic['nome'] = (input('Nome: '))
    dic['idade'] = int(input('Idade: '))
    dic['sexo'] = (input('Sexo [M/F]: '))
    res = str(input('Quer continuar? '))
    lista.append(dic)
    lista.append(dic['nome'])
    lista.append(dic['idade'])
    lista.append(dic['sexo'])
    if res == 'N':
        break
med = soma / pessoas
print(lista)
print(f'O grupo tem {pessoas} pessoas')
print(f'A media de idade é {med} anos')
print(dic["sexo"])
