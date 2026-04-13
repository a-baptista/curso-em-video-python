maior = 0
menor = 0

for c in range (1, 6 ):
    peso = float(input(f'Qual é o peso da {c}ª pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if  peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O peso maior foi de {maior:.1f}kg.')
print(f'E o peso menor foi de {menor:.1f}kg.')
