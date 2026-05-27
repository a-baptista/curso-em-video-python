num = 0
soma = 0
contador = 0

while num != 999:
    num = int(input('Digita um número inteiro: '))
    if num == 999:
        break
    contador += 1
    soma += num

print(f'Foram digitados {contador} números, e a soma entre eles foi {soma}.')
