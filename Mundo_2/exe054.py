from datetime import date
cont_maior = 0
cont_menor = 0
atual = date.today().year

for c in range(1, 8):
    data = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    diferenca = atual - data
    if diferenca >= 18:
        cont_maior += 1
    else:
        cont_menor += 1
print (f'Houve {cont_maior} pessoas maiores de idade.')
print (f'E houve {cont_menor} pessoas menores de idade.')
