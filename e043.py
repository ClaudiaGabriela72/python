vproduto = float(input('Qual é o valor do produto que voce quer comprar?'))
print("""1- Á vista 
2-Á vista no cartão 
3-Até \033[31m2\033[m(duas) veses no cartão 
4-Até \033[31m3\033[m(tres) veses no cartão""")
esco = int(input('Escolha a forma de pagamento:'))

if esco == 1:
    des = vproduto - (vproduto * 10 / 100)
    print('O valor que voce ira pagar é \033[35m{}\033[m'.format(des))

elif esco == 2:
    des = vproduto -(vproduto * 5 / 100)
    print('O valor que voce ira pagar é \033[35m{}\033[m'.format(des))

elif esco == 3:

    print('O valor que voce ira pagar é \033[35m{}\033[m'.format(vproduto))

elif esco == 4:
   des = des = vproduto + (vproduto * 20 /100)
   print('O valor que voce ira pagar é \033[35m{}\033[m'.format(des))

else:
    print('Essa poção é invalida')
