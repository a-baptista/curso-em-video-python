from random import shuffle
a1 = input ('o nome do primeiro aluno:')
a2 = input ('O nome do segundo aluno:')
a3 = input ('O nome do terceiro aluno:')
a4 = input ('O nome do quarto aluno:')
ordem =  [a1, a2, a3, a4]
shuffle (ordem)
print ('A ordem de apresentação será {}'.format(ordem))







