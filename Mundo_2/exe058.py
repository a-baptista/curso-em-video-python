from random import randint
from time import sleep

print('\033[33m-=-\033[m' * 25)
print('\033[34m      🤖 COMPUTADOR: "VOU PENSAR NUM NÚMERO DE 0 A 10..."\033[m')
print('\033[33m-=-\033[m' * 25)
sleep (0.5)
print('Achas que consegues adivinhar qual é?')
print('\033[33m-=-\033[m' * 25)
sleep (0.5)
jogador = int(input('Diz-me o teu palpite? '))
computador = randint(0, 10)
cont_tentativas = 1

while jogador != computador:
    if jogador > computador:
        print ('Tenta um número MENOR...⬇️')
        jogador = int(input('Qual é o teu palpite? '))
        cont_tentativas += 1
    if jogador < computador:
        print ('Tenta um número MAIOR...⬆️')
        jogador = int(input('Qual é o teu palpite? '))
        cont_tentativas += 1

print('\n\033[32m' + '⭐' * 25)
print(f'   🎯 ¡PARABÉNS! ACERTASTE!')
print(f'   Foram necessárias {cont_tentativas} tentativas.')
print('⭐' * 25 + '\033[m')

if cont_tentativas == 1:
    print('🏆 SENSACIONAL! Acertaste à primeira! És um mestre!')
elif cont_tentativas <= 4:
    print('👏 Muito bem! Tens uma excelente intuição.')
else:
    print('😅 Finalmente! Precisas de praticar mais a tua pontaria.')