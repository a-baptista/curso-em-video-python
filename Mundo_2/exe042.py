print ('-=-' * 20)
print ('ANALISADOR DE TRIÂNGULOS')
print ('-=-' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print ('Os segmentos acima PODEM formar um triângulo ', end='')
    if r1 == r2 == r3:
        print ('EQUILÁTERO.')
    elif r1 != r2 and r2 != r3 and  r1 != r3:
        print ('ESCALENO.')
    else:
        print ('ISÓSCELES.')
else:
    print ('NÃO PODE formar qualquer tipo de triângulo.')

