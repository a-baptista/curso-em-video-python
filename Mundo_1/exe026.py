a = str(input('Faça uma frase: ')).strip().upper()
a1 = a.count('A')
a2 = a.find('A') + 1
a3 = a.rfind('A') + 1
print ('O "A" aparece {} vezes.'.format(a1))
print ('O "A" aparece a primeira vez na posição {}.'.format(a2))
print ('O "A" aparece pela última vez na posição {}.'.format(a3))




