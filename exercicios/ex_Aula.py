idade = int(input('Qual a sua idade?'))

   
if idade==16 or idade ==17:
    print('Eleitor facultativo.')
elif idade<=65 and idade >=18:
    print('Eleitor obrigatorio.')
elif idade>65:
    print('Eleitor facultativo')
else:
    print('Não-Eleitor.')

