import datetime
a = int (input ('Ano de nascimento: '))
atual = datetime.date.today().year
idade = atual - a
print ('Quem nasceu em {} tem {} anos em {}.'.format(a, idade, atual))
if idade < 18:
    passado = 18 - idade
    ano_falta = atual + passado
    print ('Ainda falta {} anos para o alistamento.'.format(passado))
    print ('E o teu alistamento será em {}.'.format(ano_falta))
elif idade > 18:
    passou = idade - 18
    ano_passado = atual - passou
    print ('Já deverias ter alistado há {} anos.'.format(idade - 18))
    print ('O teu alistamento foi em {}'.format(ano_passado))
else:
    print ('Tens de te alistar JÁ!!!')


