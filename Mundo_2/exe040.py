a = float (input('Primeira nota: '))
b = float (input('Segunda nota: '))
media = (a + b) / 2
print ('A nota {} e a nota {} dá uma média de {}'.format(a, b, media))
if media >= 16:
    print ('Parabéns conseguiste passar de ano com uma média bastante boa!')
elif media >=10:
    print ('Parabéns, conseguiste passar de ano.')
else:
    print ('Reprovaste, espero que consigas da próxima vez!')

