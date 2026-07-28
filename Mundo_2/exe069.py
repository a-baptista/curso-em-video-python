#Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
#  No final, mostre:

#A) quantas pessoas tem mais de 18 anos.

#B) quantos homens foram cadastrados.

#C) quantas mulheres tem menos de 20 anos.
from time import sleep

maioridade = 0
numero_homens = 0
numero_mulheres_menos_20 = 0

print( '=' * 50)
print('📝 Registo de pessoas 📝'.center(50))
print( '=' * 50)

while True:
    sleep(1)

    idade = int(input('Digite a idade da pessoa: '))

    sleep(0.5)

    sexo = input('Digite o sexo da pessoa (M/F): ').strip().lower()[0]

    if idade > 18:
        maioridade += 1

    if sexo == 'm':
        numero_homens += 1

    if sexo == 'f' and idade < 20:
        numero_mulheres_menos_20 += 1

    print('=' * 50)
    sleep(0.5)
    continuar = input('Deseja registar outra pessoa? (S/N): ').strip().lower()[0]
    print('=' * 50)
    if continuar == 'n':
        break

sleep(1)
print( '=' * 50)
print('📊 Estatísticas 📊'.center(50))
print( '=' * 50)

sleep(1)

print(f'⬆️ A quantidade de pessoas com mais de 18 anos é: {maioridade} pessoas. ⬆️')
sleep(0.5)
print(f'👨🏼‍🦱 O total de pessoas do sexo masculino registados é: {numero_homens} homens. 👨🏼‍🦱')
sleep(0.5)
print(f'👩🏼‍🦱 A quantidade de mulheres com menos de 20 anos é: {numero_mulheres_menos_20} mulheres. 👩🏼‍🦱')
print( '=' * 50)
