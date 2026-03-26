distancia = int (input('Qual vai ser a distância da viagem? '))
preco = distancia * 0.50
if distancia <= 200:
    print('Com {}km de viagem, o bilhete tem um custo de {:.2f}€'.format(distancia, preco))
else:
    preco1 = distancia * 0.45
    print('Como são {}km, o bilhete tem um custo de {:.2f}€'.format(distancia,preco1))



