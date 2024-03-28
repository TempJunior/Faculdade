import math
a = int(input('Digite um valor inteiro.'))
b = int(input('Digite outro valor inteiro.'))
c = int(input('Digite outro valor inteiro.'))

delta = b**2 - 4*a*c

raiz1 = (-b + math.sqrt(delta))/(2*a)
raiz2 = (-b - math.sqrt(delta))/(2*a)

if delta >=0:
    print('Não há raizes reais.')
elif a ==0:
    print('Não é equaçao de segundo grau.')