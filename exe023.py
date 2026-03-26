num = int (input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print ('unidade: {}'.format(u))
print ('dezena: {}'.format(d))
print ('centena: {}'.format(c))
print ('milhar: {}'.format(m))

#prof fez em formato texto também
num = int (input('Informe um número: '))
n = str(num)
print ('Analisando o número {}'.format(num))
print ('Unidade: {}'.format(n[3]))
print ('Dezena: {}'.format(n[2]))
print ('Centena: {}'.format(n[1]))
print ('Milhar: {}'.format(n[0]))
