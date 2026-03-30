n1 = float (input('Quanto recebes de ordenado?'))
o = n1 * 1.15
print ('O teu ordenado era {:.2f}€ com o aumento de 15% será de {:.2f}€'.format(n1,o))

salário = float(input('Qual é o salário do Funcionário?'))
novo = salário + (salário * 15/100)
print ('Um funcionário que ganhava {:.2f}€, com 15% de aumento, passa a receber {:.2f}€.'.format(salário,novo))

produto = float(input('Quanto custa o produto?'))
d = produto * 0.90
total = produto * 1.08
total_com_juro = total / 12
print ('Se pagar o produto na totalidade fica com um desconto de 10%, ou seja, {:.2f}€.'.format(d))
print('Se pagar em prestações ficará {:.2f}€ por mês com um juro acrescido de 8%.'.format(total_com_juro))




