soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digita o {}º valor: '.format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Informaste {} números pares e a sua soma é de {}.'.format(cont, soma))
