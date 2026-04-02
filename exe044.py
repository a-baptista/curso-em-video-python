print ('-=-' * 10, 'Loja da Andreia', '-=-' * 10)
produto = float (input('Total da compra: '))
print ('-' * 3, 'Forma de pagamento', '-' * 3)
print ('[1] pagamento em dinheiro/cheque.')
print ('[2] pagamento em cartão.')
print ('[3] pagamento 2x em cartão.')
print ('[4] pagamento 3x ou mais em cartão.')
print ('-' * 25)
opcao = int (input('Opção: '))
if opcao == 1:
    desconto10 = produto * 0.10
    preco_final = produto - desconto10
    print ('Pagamento em dinheiro/cheque vai ser de {:.2f}€ com 10% de desconto.'.format(preco_final))
elif opcao == 2:
    desconto5 = produto * 0.05
    preco_final = produto - desconto5
    print ('Pagamento em cartão vai ser de {:.2f}€ com 5% de desconto.'.format(preco_final))
elif opcao ==3:
    prestacao = produto / 2
    print ('Pagamento 2x em cartão vai ser de {:.2f}€'.format(prestacao))
elif opcao == 4:
    vezes = int (input ('Em quantas vezes deseja pagar: '))
    juros = produto + (produto * 0.20)
    total = juros / vezes
    print ('Pagamento em {}x vai ser de {:.2f}€ com 20% de juros.'.format(vezes,total))
    print ('A sua compra de {:.2f}€ vai-lhe custar no final {:.2f}€.'.format(produto,juros))
else:
    print('Opção Inválida!')
