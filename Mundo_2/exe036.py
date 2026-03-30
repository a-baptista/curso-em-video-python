valor_casa = float(input('Qual o valor da casa? €'))
salario = float(input('Qual o salário do comprador? €'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = valor_casa / (anos * 12)
taxa_esforco = salario * 0.30
print ('Para pagar uma casa no valor de {:.2f}€, em {} anos, tem um valor mensal de {:.2f}€'.format(valor_casa, anos, prestacao))
if prestacao <= taxa_esforco:
    print ('O empréstimo foi APROVADO!')
else:
    print ('O empréstimo foi REPROVADO!')
