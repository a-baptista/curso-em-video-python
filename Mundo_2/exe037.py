print( '\033[34m-=-\033[m' * 20)
num = int (input('Digita um valor inteiro qualquer: '))
print ('Escolhe uma das bases para conversão: ')
print ('Opção [1] converter para Binário')
print ('Opção [2] converter para Octal')
print ('Opção [3] converter para Hexadecimal')
binario = bin (num) [2:]
octal = oct (num) [2:]
hexadecimal = hex (num) [2:]
opcao = int (input('Qual a sua opção: '))
if opcao == 1:
    print ('O valor {}, convertido para Binário é {}'.format(num,binario))
elif opcao == 2:
    print ('O valor {}, convertido a Octal é de {}'.format(num, octal))
elif opcao == 3:
    print ('O valor {}, convertido a Hexadecimal é de {}'.format(num, hexadecimal))
else:
    print ('Opção inválida.')






