peso = float (input ('Qual o seu peso: '))
altura = float (input ('Qual a sua altura: '))
imc = peso / (altura * altura)
print ('O seu peso é {}kg e a sua altura é {}m, logo o seu IMC é de {:.1f}.'.format(peso, altura, imc))
if imc < 18.5:
    print ('Está abaixo do peso.')
elif imc >= 18.5 and imc <= 25:
        print ('Está no peso ideal.')
elif imc >= 25 and imc <= 30:
        print ('Está em sobrepeso.')
elif imc >= 30 and imc <= 40:
        print ('Está em obesidade.')
else:
    print ('Está em obesidade mórbida.')

