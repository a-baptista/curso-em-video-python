contador = 0
soma = 0
resposta = 'S'

while resposta == 'S':
    num = int(input('Digite um valor: '))
    soma += num
    contador += 1

    if contador == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resposta == '':
        resposta = 'N'
    else:
        resposta = resposta [0]

media = soma / contador
    
print(f'Foram digitados {contador} valores.')
print(f'A média dos valores foi {media:.2f}.')
print(f'O maior valor foi {maior}.')
print(f'O menor valor foi {menor}.')
