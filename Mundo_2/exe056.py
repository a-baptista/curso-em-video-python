print ('-=-' * 10)
print ('ANALISADOR COMPLETO')
print('-=-' * 10 )
soma_idade = 0
media = 0
maior_idade_homem = 0
nome_velho = ''
cont_mulher = 0
idade_menor20 = 0

for p in range(1,5):
    print (f'**** Dados da {p}ª pessoa ****')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str (input('Sexo[M/F]: ')).upper().strip()
    soma_idade += idade
    if p ==1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        cont_mulher += 1

media = soma_idade / 4
print('-=-' * 20)
print (f'A média de idade do grupo é de {media:.1f} anos.')
print(f'O nome do homem mais velho é {nome_velho} e tem {maior_idade_homem} anos.')
print(f'No total são {cont_mulher} mulheres que têm menos de 20 anos.')
