velocidade = int(input('Qual a velocidade do carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print ('Passou o limite nesta estrada indo a {} Km/H, a sua multa é de {:.2f}€.'.format(velocidade,multa))
else:
    print ('Boa viagem!')
print ('Dirija com segurança!')

