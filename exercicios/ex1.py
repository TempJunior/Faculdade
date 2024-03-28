peso = float(input('Qual o seu peso?'))
altura = float(input('Qual a sua altura?'))
imc = peso/altura**2

if imc <20:
    print('Voce esta abaixo do peso.')
elif imc <=25 or imc <30:
    print('Voce esta no peso normal.')
elif imc <=35 or imc <40:
    print('Voce esta em sobrepeso')
elif imc <=45:
    print('Obeso.')
else:
    print('Obeso morbito.')
print(f'Seu percentual é: {imc:.2f}')

