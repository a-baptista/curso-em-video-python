print ('🔢TABUADA🔢')
print ('-' * 20)
n = int(input('Digita um valor: '))
for c in range (1, 11):
    resultado = n * c
    print('{} X {:2} = {}'.format(n, c, resultado))
print ('-' * 20)