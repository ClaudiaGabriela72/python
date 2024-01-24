import math
cop = int(input('Qual é o valor do cateto oposto? '))
cad = int(input("Qual é o valor do cateto adejasente ? "))
hi = math.hypot(cop, cad)
print('A hipotenusa de um triangulo retangulo que tem {} no cateto oposto e {} no adejasente tem  {:.2f}de hipotenusa'.format(cop, cad, hi))

