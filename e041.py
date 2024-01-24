from datetime import date
anon = int(input('Qual foi o ano do seu nascimento? '))
cal = date.today().year - anon

if cal <= 9:
    print('Voce esta com {} anos por isso esta na categoria mirim'.fotmat(cal))

elif cal <= 14:
    print('Voce esta na categoria infantil')

elif cal <= 19:
    print('Voce esta na categoria junior ')

elif cal <= 20:
    print('Voce esta na categoria senior ')
else:
    print('Voce esta na categoria senior ')

print(cal)
