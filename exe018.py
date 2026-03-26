from math import sin, cos, tan, radians
angulo = float(input('Qual o ângulo?'))
angulo_rad = radians (angulo)
s = sin (angulo_rad)
c = cos (angulo_rad)
t = tan (angulo_rad)
print('O ângulo {}, tem o seno de {:.2f}, cosseno {:.2f} e a tangente de {:.2f}.'.format (angulo,s,c,t))

