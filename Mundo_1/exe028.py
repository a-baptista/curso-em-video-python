from random import randint
computador = randint(0, 5)
jogador = int(input('Escolhe um número de 0 a 5: '))
if jogador == computador:
    print('BOA ACERTASTE!!Esse foi o número que eu escolhi {}.'.format(computador))
else:
    print('NAHH!!PERDESTE!!Eu pensei no {} e não no {}!'.format(computador,jogador))

#professor:
from random import  randint
from time import sleep
computador = randint(0, 5) #Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))

