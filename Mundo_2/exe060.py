#Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
#5! = 5 x 4 x 3 x 2 x 1 = 120
n = int (input('Digita um valor: '))
contador = n
f = 1

print(f'A calcular {n}! = ' , end='')
while contador > 0:
    print (f'{contador}', end='')
    f *= contador
    if contador > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    contador -= 1
print(f'{f}')
