from time import sleep
print('\033[33m=' * 40)
print(f'{"🔢 CALCULADORA PRO v1.0":^40}')
print('=' * 40 + '\033[m')

num1 = float (input('Digita o 1º valor👉: '))
num2 = float(input('Digita o 2º valor👉: '))
opcao = 0
sleep (1)
while opcao != 5:
    print('\n\033[34m┌' + '─' * 38 + '┐')
    print(f'│{"MENU DE OPERAÇÕES":^38}│')
    print('├' + '─' * 38 + '')
    print('├[1] SOMAR')
    print('├[2] MULTIPLICAR')
    print('├[3] MAIOR NÚMERO')
    print('├[4] NOVOS NÚMEROS')
    print('├[5] SAIR')
    print('└' + '─' * 38 + '┘\033[m')
    sleep(0.5)

    opcao = int(input('\033[1m>>>> Qual é a sua opção? \033[m'))
    sleep(0.5)

    print('\033[37m' + '·' * 40 + '\033[m')

    if opcao == 1:
        soma = num1 + num2
        sleep(0.5)
        print (f'{num1:.1f} + {num2:.1f} = {soma:.1f}')
        sleep(1)
    elif opcao == 2:
        multiplicar = num1 * num2
        sleep(0.5)
        print (f'{num1:.1f} * {num2:.1f} = {multiplicar:.1f}')
        sleep(1)
    elif opcao == 3:
        sleep(0.5)
        if num1 > num2:
         print (f'O maior número é {num1:.1f}.')
         sleep(1)
        elif num2 > num1:
            print (f'O maior número é {num2:.1f}.')
            sleep(1)
        else:
            print ('Os dois números são iguais.')
            sleep(1)
    elif opcao == 4:
        sleep(0.5)
        print('\033[36m🔄 A reiniciar valores...\033[m')
        num1 = float (input('Digita O 1º valor👉: '))
        num2 = float (input('Digita O 2º valor👉: '))
        print('\033[32mValores atualizados com sucesso!\033[m')
        sleep(1)
    elif opcao == 5:
        sleep(0.5)
        print('\033[31m✨ A encerrar... Até breve!\033[m')
    else:
        sleep(1)
        print('\033[1;31m⚠️ OPÇÃO INVÁLIDA!\033[m')
        print('Por favor, escolhe um número entre 1 e 5.')
        sleep(1.5)

sleep(1)
print('\n\033[33m' + '═' * 40)
print(f'{"OBRIGADO POR USAR A NOSSA CALCULADORA":^40}')
print('═' * 40 + '\033[m')
