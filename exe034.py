salario = float(input('Qual é o seu salário? '))
if salario >= 1250:
    aumento10 = salario * 1.10
    print ('Quem ganha {:.2f}€ passa a receber {:.2f}€'.format(salario, aumento10))
else:
    aumento15 = salario * 1.15
    print ('Quem ganha {:.2f}€ passa a receber {:.2f}€'.format(salario, aumento15))