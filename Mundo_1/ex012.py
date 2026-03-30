n1 = float (input('Preço do produto:'))
d = n1 * 0.95
print ('O preço final do produto, já com o desconto de 5%, fica a {:.2f}€.'.format(d))

preço = float(input('Qual é o preço do produto:'))
novo = preço - (preço * 5 / 100)
print ('O produto que custava {:.2f}€, na promoção com desconto de 5% vai custar {:.2f}€.'.format(preço,novo))
