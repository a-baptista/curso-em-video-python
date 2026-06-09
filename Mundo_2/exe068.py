from random import randint
from time import sleep 

contador_vitorias = 0

print('🎲 PAR OU ÍMPAR 🎲')
while True:
    num_computador = randint (0, 10)
    sleep (1)
    jogador = int(input('🎲 Digita um número: '))
    sleep (1) 
    escolha = str(input('🎲 Par ou Ímpar? [P/I] ')).strip().upper()[0]

    total = jogador + num_computador
    resultado = 'P' if total % 2 == 0 else 'I'
    texto_resultado = 'PAR' if resultado == 'P' else 'ÍMPAR'

    sleep (1.5)

    print(f'🎉 Você jogou {jogador} e o computador {num_computador}. Total deu {total} e por isso é {texto_resultado}. 🎉')

    if escolha == resultado:
        sleep (1.5)
        print('✨🥇 GANHASTE!🥇✨ ')
        contador_vitorias += 1
    else:
        sleep (1.5)
        print('💣💥 PERDESTE! 💥💣')
        break

print(f'✨ GAME OVER! Você venceu {contador_vitorias} vezes. ✨') 
