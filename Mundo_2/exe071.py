from time import sleep

print("=" * 50)
print("🏧  REDE MULTIBANCO  🏧".center(50))
print("=" * 50)
print("💳 Cartão inserido com sucesso!".center(50))
print("=" * 50)
sleep(1)

valor_utilizador = 1300.00

while True:
    print("\n" + "=" * 50)
    print("📌  MENU PRINCIPAL  📌".center(50))
    print("=" * 50)
    print(" [ 1 ] 💶 Levantamentos")
    print(" [ 2 ] 📊 Consultar Saldo")
    print(" [ 3 ] 💸 Transferências")
    print(" [ 4 ] 🧾 Pagamentos e Serviços")
    print(" [ 5 ] 📥 Depósito de Valores")
    print(" [ 6 ] 🚪 Sair / Cancelar")
    print("=" * 50)

    opcao = int(input("👉 Escolha a opção pretendida (1-6): "))

    if opcao == 1:
        print("\n" + "─" * 50)
        print("💶  ÁREA DE LEVANTAMENTO  💶".center(50))
        print("─" * 50)
        print("💡 Notas disponíveis: 10€ | 20€ | 50€")
        print("📌 Opções rápidas: 10€ | 20€ | 50€ | 100€ | 150€ | 200€ | 400€")
        print("─" * 50)

        valor_levantamento = int(input("💶 Qual o valor que deseja levantar? €"))

        if valor_levantamento <= 0:
            print("⚠️ Valor inválido. Por favor, insira um valor positivo.")

        elif valor_levantamento > valor_utilizador:
            print("❌ Saldo insuficiente para realizar a operação.")

        elif valor_levantamento % 10 != 0:
            print("⚠️ Operação recusada! Apenas são permitidas notas de 10€, 20€ e 50€.")

        else:
            valor_utilizador -= valor_levantamento
            print("\n⏳ A processar as suas notas...")
            sleep(1.2)

            total_valor = valor_levantamento
            nota = 50
            total_notas = 0 

            while True:
                if total_valor >= nota:
                    total_valor -= nota
                    total_notas += 1
                else:
                    if total_notas > 0:
                        print(f"   💵 Entregue: {total_notas} nota(s) de {nota}€")
                    
                    if nota == 50:
                        nota = 20
                    elif nota == 20:
                        nota = 10
                    
                    total_notas = 0

                    if total_valor == 0:
                        break

            print("\n" + "─" * 50)
            print("✅ Levantamento concluído com sucesso!")
            print(f"💰 Saldo atual disponível: {valor_utilizador:.2f}€")
            print("─" * 50)

    elif opcao == 2:
        print("\n" + "─" * 50)
        print("📊  CONSULTA DE SALDO  📊".center(50))
        print("─" * 50)
        print("⏳ A consultar a sua conta...")
        sleep(0.8)
        print(f"💰 Saldo Contabilístico / Disponível: {valor_utilizador:.2f}€")
        print("─" * 50)

    elif opcao == 3:
        print("\n" + "─" * 50)
        print("💸  TRANSFERÊNCIAS BANCÁRIAS  💸".center(50))
        print("─" * 50)
        iban = input("👉 Introduza o IBAN ou NIB do destinatário (ex: PT50...): ").strip().upper()

        if len(iban) <= 10:
            print("❌ IBAN/NIB inválido. Por favor, insira um IBAN/NIB correto.")

        else:
            valor_transferencia = float(input("💶 Qual o valor que deseja transferir? (€): "))

            if valor_transferencia > valor_utilizador:
                print("❌ Saldo insuficiente para esta transferência.")

            elif valor_transferencia <= 0:
                print("⚠️ Valor inválido.")
            
            else:
                valor_utilizador -= valor_transferencia
                print("\n⏳ A comunicar com a rede interbancária...")
                sleep(1.5)
                print("\n" + "─" * 50)
                print(f"✅ Transferência de {valor_transferencia:.2f}€ realizada com sucesso!")
                print(f"👤 Destinatário: {iban}")
                print(f"💰 Saldo restante: {valor_utilizador:.2f}€")
                print("─" * 50)

    elif opcao == 4:
        print("\n" + "─" * 50)
        print("🧾  PAGAMENTO DE SERVIÇOS  🧾".center(50))
        print("─" * 50)
        entidade = input("👉 Entidade (5 dígitos): ").strip()
        referencia = input("👉 Referência (9 dígitos): ").strip()

        if len(entidade) != 5 or not entidade.isdigit() or len(referencia) != 9 or not referencia.isdigit():
            print("❌ Entidade ou referência inválida! Verifique os dados do talão.")
        else:
            montante = float(input("💶 Montante (€): "))

            if montante <= 0:
                print("⚠️ Valor inválido.")
            elif montante > valor_utilizador:
                print("❌ Saldo insuficiente.")
            else:
                valor_utilizador -= montante
                print("\n⏳ A comunicar com a entidade prestadora de serviços...")
                sleep(1.5)
                print("\n" + "─" * 50)
                print("✅ Pagamento efetuado com sucesso!")
                print(f"🏢 Entidade: {entidade} | 🔢 Ref: {referencia[:3]} {referencia[3:6]} {referencia[6:]}")
                print(f"💶 Montante pago: {montante:.2f}€")
                print(f"💰 Saldo restante: {valor_utilizador:.2f}€")
                print("─" * 50)

    elif opcao == 5:
        print("\n" + "─" * 50)
        print("📥  DEPÓSITO DE VALORES  📥".center(50))
        print("─" * 50)
        deposito = float(input("💶 Indique o valor em notas a introduzir na ranhura (€): "))

        if deposito < 5 or deposito % 5 != 0:
            print("⚠️ O Multibanco apenas aceita notas válidas (múltiplos de 5€).")
        else:
            print("\n⏳ A validar e a contar as notas inseridas...")
            sleep(1.5)
            valor_utilizador += deposito
            print("\n" + "─" * 50)
            print("✅ Depósito realizado com sucesso!")
            print(f"📥 Foi depositado um total de: {deposito:.2f}€")
            print(f"💰 Novo saldo disponível: {valor_utilizador:.2f}€")
            print("─" * 50)


    elif opcao == 6:
        print("\n" + "─" * 50)
        print("⏳ A devolver o seu cartão... Por favor, retire o cartão da ranhura.")
        sleep(1.2)
        print("✨ Obrigado por utilizar a Rede Multibanco. Até à próxima! 👋")
        print("─" * 50)
        break

    else:
        print("⚠️ Opção inválida! Escolha um número entre 1 e 6.")

    sleep(1)