n1 = float(input('Valor em metros:'))
cm = n1 * 100
mm = n1 * 1000
print ('{} metros são {} centímetros e {} milimetros.'.format(n1,cm,mm))

print('-' * 20)
n = float(input('Valor em metros:'))
km = n / 1000
hm = n / 100
dam = n / 10
dm = n * 10
cm = n * 100
mm = n * 1000
print ('{}m são:\n{}km;\n{}hm;\n{}dam;\n{}dm;\n{}cm;\n{}mm.'.format(n,km,hm,dam,dm,cm,mm))
print ('-' * 20)


