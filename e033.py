n1a = int(input('Digite um numero '))
n2b = int(input('Digite outro numero '))
n3c = int(input('Digite mais um '))
menor = n1a
if n2b < n1a and n2b < n3c:
    menor = n2b
if n3c < n1a and n3c < n2b:
    menor = n3c

maior = n1a

if n2b > n1a and n2b > n3c:
    maior = n2b
if n3c > n1a and n3c > n2b:
    maior = n3c
print('o menor valor digitado foi {}'.format(menor))
print('O maior foi {}'.format(maior))
