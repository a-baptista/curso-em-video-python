num = int(input('Digita um número [Para parar digite 999]: '))

contador = 0
soma = 0

while num != 999:
    
    soma += num
    contador += 1
    num = int(input('Digita um número [Para parar digite 999]: '))
    
print(f'Foram digitados {contador} números e a soma entre eles foi de {soma}.')
