nome = str(input('Escreva seu nome completo... ')).strip()
print('seu nome em letras Maiusculas', nome.upper())
print('Seu nome em letras minuscualas', nome.lower())
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {}'.format(nome.find(' ')))
ps = nome.split()
print(len(ps[0]))

