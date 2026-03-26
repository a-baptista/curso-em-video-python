n1 = float (input ('Quantos metros de largura tem a parede?'))
n2 = float (input ('Quantos metros de altura tem a parede?'))
a = n1 * n2
t = a / 2
print ('É necessário {:.1f} litros de tinta para {} metros² de área.'.format(t,a))

larg= float (input('Largura da parede:'))
alt = float (input('Altura da parede:'))
área= larg * alt
print ('A sua parede tem a dimensão de {}x{} e a sua área é de {:.1f}m².'.format(larg,alt,a))
tinta = área / 2
print ('Para pintar essa parede, você precisará de {:.1f}l de tinta.'.format (tinta))


