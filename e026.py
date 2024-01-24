frase = str(input('escreva uma frase ')).lower().strip()

#print(frase)
#am = frase.count('a')

print('tem {} letras a '.format(frase.count('a')))
print('a primeira letra a aparece na possiçao {}'.format(frase.find('a') + 1))
print('a ultima leatra a aparec na possiçao {}'.format(frase.rfind('a')))
