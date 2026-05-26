print('-' * 30)
print(f'{"SEQUÊNCIA DE FIBONACCI":^30}')
print('-' * 30)

num = int(input('Digita um número: '))

contador = 0
a = 0
b = 1
c = 0

while contador < num:
    print(f'{c} ->', end = ' ')
    a = b
    b = c
    c = a + b 
    contador += 1

print('FIM')
print('-' * 30)