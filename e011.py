largura = float(input('Qual a largura da sua parede (metros) ? '))
altura = float(input('Qual a altura da sua parede (metros)? '))
area = largura * altura
print('Sua parede tem a dimensao de {}x{} e a sua aréa é de {}m2'.format(largura, altura, area))
tin = area / 2
print('Você precisara de {} Litros para pintar a sua parede'.format(tin))