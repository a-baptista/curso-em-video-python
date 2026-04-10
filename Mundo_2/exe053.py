frase = str(input('Digite uma frase: ')).strip().upper().split()
juntar = ''.join(frase)
inverso = juntar[::-1]
print(f'A frase digitada foi {inverso}')

if inverso == juntar:
    print('É PALÍNDROMO!!')
else:
    print('NÃO é PALÍNDROMO!')
