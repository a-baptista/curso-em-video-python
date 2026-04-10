cont = 0
n = int (input('Digite um número: '))

for c in range(1, n + 1 ):
    if n % c == 0:
        cont += 1
        print('\033[33m', end=' ')
    else:
        print('\033[31m', end=' ')
    print(f'{c} ', end='')

print(f'\n\033[mO número {n} foi divisivel {cont} vezes.')
if cont == 2:
    print ('É número primo!')
else:
    print ('Não é número primo!')
