from time import sleep

while True:
    print('=' * 45)
    sleep(1)
    num = int(input('Digita um número para ver a sua tabuada: '))
    sleep(1)
    print('=' * 45)
    
    if num < 0:
        print('\n🛑 PROGRAMA DE TABUADA ENCERRADO. Volta sempre! 👋')
        print('=' * 50)
        break

    print(f'📊 TABUADA DO {num} 📊: ')
    sleep(1)
    print('-' * 25)
    for x in range(1, 11):
        print(f'{num} x {x:2} = {num * x}')
    print('-' * 25)    
