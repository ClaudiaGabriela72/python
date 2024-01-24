list = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    nota = nota1 + nota2
    med = nota / 2
    list.append([nome, nota, med])
    res = str(input('Quer continuar? '))
    if res in 'N':
        break

for i, a in enumerate(list):
    print(f'{i} {a[0]}     {a[2]}')
