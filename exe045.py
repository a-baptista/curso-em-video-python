from random import choice
from time import sleep
print ('👊 ✋ ✌️ PEDRA PAPEL TESOURA 👊 ✋ ✌️')
itens = ('👊', '✋', '✌️')
computador = choice(itens)
print ('[1] Pedra 👊')
print ('[2] Papel ✋')
print ('[3] Tesoura ✌️')
jogador_num = int(input('Qual escolhes? '))
jogador = itens[jogador_num - 1]
print ('PEDRA')
sleep (1)
print ('PAPEL')
sleep (1)
print ('TESOURA!!!!')
sleep (1.5)
print ('👾' + '─' * 20 + '👾')
print ('Computador escolheu {}'.format(computador))
print ('Tu escolheste {}'.format(jogador))
print ('👾' + '─' * 20 + '👾')
if computador == jogador:
    print ('EMPATE')
elif (jogador == '👊' and computador == '✌️') or \
     (jogador == '✋' and computador == '👊') or \
     (jogador == '✌️' and computador == '✋'):
    print ('GANHASTE!! Aqui tens um biscoito 🍪🏆')
else:
    print ('PERDESTE!!🤖')
