from datetime import date
ano = int(input('Qual o ano do seu nascimento? '))
anoat = date.today().year
cal = anoat - ano

if cal < 18:
    print('\033[35mVoce ainda tera que se alistar no futuro!\033[m')

elif cal > 18:
    print('Voce ja tem ou ainda ira fazer \033[34m{}\033[m portanto ja passou do tempo de se alistar'.format(cal))

else:
    print('Voce tem \033[31m18\033[m ja pode se alistar')
print(cal)
