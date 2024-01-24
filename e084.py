leve = []
pesado = []
pessoa = []
galera = []
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(int(input('Peso: ')))
    cont = str(input('Quer continuar? '))
    galera.append(pessoa)
    if cont == "N":
        break
    if pessoa == 100:
        pesado.append(pessoa)
    if pessoa == 70:
        leve.append(pessoa)
print(pesado)
print(leve)
print(pessoa)

