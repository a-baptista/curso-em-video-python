print ('-=-' * 10)
print ('10 TERMOS  DE PA')
print ('-=-' * 10)
primeiro_termo = int(input('Digita o primeiro termo: '))
razao = int(input('Digita a razão: '))
decimo = primeiro_termo + (10 - 1) * razao
for c in range (primeiro_termo, decimo + razao, razao):
    print('{}'.format(c), end =' -> ')
print('FIM')
