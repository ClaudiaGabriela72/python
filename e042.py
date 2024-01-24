altura = float(input('Qual a sua altura?(metros)'))
peso = float(input('Qual o seu peso ?(Kg)'))
cal = (peso / altura**2)

if cal < 18.5:
    print('Voce esta abaixo do peso')

if 18.5 < cal < 25:
    print('Voce esta no peso ideal')

elif 25 < cal < 30:
    print('Voce esta com \033[1;32Sobre pesso')
elif 30 < cal < 40:
    print('Voce esta \033[1;31OBESSO')

else:
    print('Voce esta com obssidade morbida ')
print('Seu IMC é de {:.2f}'.format(cal))

