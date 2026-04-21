print ('-=-' * 10)
print (f'{'10 TERMOS DE PA V2.0':^30}')
print ('-=-' * 10)
primeiro_termo = int(input('Primeiro termo: '))
razao = int (input('Digita a razão: '))
contador = 1
termo = primeiro_termo

while contador <= 10:
    print(f'{termo} -> ', end='')
    contador += 1
    termo += razao

print('FIM')
