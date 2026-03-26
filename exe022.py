nome = str(input('Qual é o seu nome completo? ')).strip()
m = nome.upper()
print ('O nome completo é {}.'.format(nome))
print ('O nome completo com todas as letras em Maiúsculas é {}.'.format(m))
mi = nome.lower()
print ('o nome completo com todas as letras em minúsculas é {}. '.format(mi))
len (nome) - nome.count('')
total = len (nome) - nome.count(' ')
print ('O nome tem {} letras ao todo.'.format(total))
nome1 = nome.find(' ')
print ('O primeiro nome tem {} letras.'.format(nome1))
dividido = nome.split()
segundo_nome = len(dividido [1])
print ('O segundo nome tem {} letras.'.format(segundo_nome))
di= nome.split()
terceiro_nome = len(di [2])
print ('O terceiro nome tem {} letras.'.format(terceiro_nome))

#Como o prof fez
nome = str (input('Digite o seu nome completo: ')).strip()
print ('Analisando o seu nome...')
print ('Seu nome em maiúsculas é {}'.format(nome.upper()))
print ('Seu nome em minúsculas é {}'.format(nome.lower()))
print ('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print ('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0],len(separa[0])))



















