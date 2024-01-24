import math
angulo = float(input('digite um angulo... '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print("O seno do angulo {} é {:.2f}\nO coseno é {:.2f}\nA tangente é {:.2f}".format(angulo, seno, cos, tangente))
