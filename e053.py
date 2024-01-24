frase = str(input('Digite uma frase: ')).strip()
palav = frase.split()
juntar = ''.join(palav)

inverso = ''
for letra in range(len(juntar) - 1, -1, -1):
    inverso += juntar[letra]

print(juntar, inverso)
if inverso == juntar:
    print('Eles sao palindromos')
else:
    print('Eles nao sao palindromos')

