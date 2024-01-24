
dic = dict()
dic['nome'] = str(input('Nome: '))
dic['ano'] = int(input('Ano de nascimento: '))
dic['carteira'] = int(input('Carteira de trabalho(0 se nao tiver): '))
dic['idade'] = 2023 - dic['ano']
del dic['ano']
if dic["carteira"] != 0:
    dic['ano da contratação'] = int(input('Ano de contratação: '))
    ap = 2023 - dic['ano da contratação']
    apo = 35 - ap
    dic['aposentadoria'] = apo + dic['idade']
    dic['salario'] = int(input('Salario: '))
for k, v in dic.items():
    print(f'{k} tem valor {v}')
print(dic)
