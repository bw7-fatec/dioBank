def main():
    saldo = 0
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3
    LIMITE_POR_SAQUE = 500

    while True:
        print("\n--- Sistema Bancário ---")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Visualizar Extrato")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Digite o valor a ser depositado: "))
            if valor > 0:
                saldo += valor
                extrato.append(f"Depósito: R$ {valor:.2f}")
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
            else:
                print("Valor inválido. O valor do depósito deve ser positivo.")

        elif opcao == "2":
            if numero_saques >= LIMITE_SAQUES:
                print("Limite diário de saques atingido.")
            else:
                valor = float(input("Digite o valor a ser sacado: "))
                if valor > 0 and valor <= LIMITE_POR_SAQUE:
                    if saldo >= valor:
                        saldo -= valor
                        extrato.append(f"Saque: R$ {valor:.2f}")
                        numero_saques += 1
                        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
                    else:
                        print("Saldo insuficiente para realizar o saque.")
                else:
                    print(f"Valor inválido. O valor do saque deve ser positivo e não pode exceder R$ {LIMITE_POR_SAQUE:.2f}.")

        elif opcao == "3":
            print("\n--- Extrato ---")
            if not extrato:
                print("Não foram realizadas movimentações.")
            else:
                for movimentacao in extrato:
                    print(movimentacao)
                print(f"Saldo atual: R$ {saldo:.2f}")

        elif opcao == "4":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()