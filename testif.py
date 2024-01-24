import random

pintura = ['Rene', 'Salvador Dali', 'Wasily Kandinsky', 'Pablo Picasso', 'Geoges Braque', 'Edvard Munch']
escultura = ['oi', 'seila']
formas = ['Wasily Kandinsky', 'Pablo Picasso', 'Salvador Dali', 'Geoges Braque']
figuras = ['René', 'Edvard Munch']
clarofor = ['Mulher com sonbrinha', 'o baile']
escurofor = ['A vampira', 'le Dejeuner sur']
pri_es = input(str('Voce prefere pinturas ou esculturas ?'))

if pri_es == 'pintura':
    seg_es = input(str('Voce prefere Formas ou Figuras?'))
    if seg_es == 'Formas':
        ran = random.choice(clarofor)
        print(f"Otimo\n A obra que mais combina com você é : {ran}")
    elif seg_es == 'Figuras':
        ran = random.choice(figuras)
        print(f'Otimo\n A obra que mais combina com você é: {ran}')
else:
    pri_es = escultura
ter_es = input('voce prefere claro ou escuro? ')
if ter_es == 'claro':
    pin = random.choice(pintura)
    print(pin)

elif ter_es == 'escuro':
    print('Perfeito')
