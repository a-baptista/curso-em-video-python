from time import sleep

contador = 0
total_gasto = 0
produto_mais_barato = ''
preco_mais_barato = 0
preco_mais_1000 = 0

print('=' * 50)
print('🛍️  PAPELARIA DA ANDREIA 📚'.center(50))
print('=' * 50)

while True:
    sleep(0.5)
    print('\n📌 Registar Item:')
    nome_produto = input('   🏷️  Nome do produto: ').strip().title()
    preco_produto = float(input('   💶 Preço do produto (€): '))

    total_gasto += preco_produto

    if preco_produto > 1000:
        preco_mais_1000 += 1

    if contador == 0 or preco_produto < preco_mais_barato:
        produto_mais_barato = nome_produto
        preco_mais_barato = preco_produto

    contador += 1

    continuar = ' '
    while continuar not in 'sn':
        continuar = input('\n   🔄 Quer registar outro produto? [S/N]: ').strip().lower()[0]

    if continuar == 'n':
        break

print('\n' + '=' * 50)
print('📊 RESUMO DA COMPRA 📊'.center(50))
print('=' * 50)

sleep(0.8)
print(f' 💳 Total gasto na compra: {total_gasto:.2f}€')
sleep(0.5)
print(f' 💎 Produtos com valor superior a 1000€: {preco_mais_1000}')
sleep(0.5)
print(f' 🏷️  Produto mais barato: {produto_mais_barato} ({preco_mais_barato:.2f}€)')

print('=' * 50)
print('✨ Obrigado por comprar na Papelaria da Andreia! ✨'.center(50))
print('=' * 50)