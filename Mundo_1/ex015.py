a = float (input('Quantos dias foi o carro utilizado:'))
b = float (input('Quantos km foram percorridos:'))
d = 60 * a
km = 0.15 * b
total = d + km
print ('O preço total é de {:.2f}€.'.format(total))

