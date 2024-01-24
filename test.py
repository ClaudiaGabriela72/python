# velhos = homem = mulher = 0
# while True:
#       print('-' * 25)
#       print('CADASTRE UMA PESSOA')
#       print('-' * 25)
#       idade = int(input('Idade: '))
#       if idade >= 18:
#             velhos += 1
#       sexo = str(input('Sexo: ')).upper().strip()[0]
#       if sexo not in 'MmFf':
#             print('Dado invalido')
#       if  idade < 20:
#             mulher += 1
#       elif sexo in 'Mm':
#             homem += 1
#       cont = str(input('Quer continuar [s/n]? '))
#       if cont in 'Nn':
#             break
# print(f'sao {mulher} mulheres com menos de 20 anos e\n '
#       f'{homem} homens cadastrados\n'
#       f'{velhos} com mais de 18 anos')

try:
      a = int(input('Numerador: '))
      b = int(input('Denominador: '))
      r = a / b
except ZeroDivisionError:
      print('Erro! nao é possivel dividir por zero.')
except ValueError:
      print('Erro! nao é possivel dividir por string')
except KeyboardInterrupt:
      print('Erro! o usuario nao digitou')
else:
      print(f'O resultado foi {r}')
















