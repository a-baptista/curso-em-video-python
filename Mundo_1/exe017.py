from math import hypot
cateto_oposto = float(input('Qual o comprimento do cateto oposto?'))
cateto_adjacente = float(input('Qual o comprimento do cateto adjacente?'))
hypot = hypot (cateto_oposto, cateto_adjacente)
print ('O comprimento da hipotenusa é de {:.2f}cm.'.format(hypot))


