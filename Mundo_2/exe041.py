from datetime import date
ano = int (input('Ano de Nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano
print ('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print ('A categoria do Atleta é MIRIM.')
elif idade <= 14:
    print ('A categoria do Atleta é INFANTIL.')
elif idade <= 19:
    print ('A categoria do Atleta é JÚNIOR.')
elif idade <= 25:
    print ('A categoria do Atleta é SÉNIOR.')
else:
    print ('A categoria do Atleta é MASTER.')
