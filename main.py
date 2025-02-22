import datetime

usuarios = []
contas = []
numero_conta_sequencial = 1

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques >= limite_saques:
        print("Limite diário de saques atingido.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    elif valor > limite:
        print(f"Valor do saque excede o limite de R$ {limite:.2f}.")
    elif valor <= 0:
        print("Valor inválido. O valor do saque deve ser positivo.")
    else:
        saldo -= valor
        data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        extrato.append(f"{data_hora} - Saque: R$ {valor:.2f}")
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    return saldo, extrato

def depositar(saldo, valor, extrato, /):
    if valor <= 0:
        print("Valor inválido. O valor do depósito deve ser positivo.")
    else:
        saldo += valor
        data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        extrato.append(f"{data_hora} - Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    return saldo, extrato

def visualizar_extrato(saldo, /, *, extrato):
    print("\n--- Extrato ---")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for movimentacao in extrato:
            print(movimentacao)
    print(f"Saldo atual: R$ {saldo:.2f}")

def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento do usuário (AAAA-MM-DD): ")
    cpf = input("Digite o CPF do usuário: ").replace(".", "").replace("-", "")
    endereco = input("Digite o endereço do usuário: ")

    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Usuário com este CPF já cadastrado.")
            return None

    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso.")
    return usuario

def criar_conta_corrente(usuario):
    global numero_conta_sequencial
    agencia = "0001"
    numero_conta = numero_conta_sequencial
    numero_conta_sequencial += 1

    conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario,
        "saldo": 0,
        "extrato": [],
        "numero_saques": 0
    }
    contas.append(conta)
    print("Conta corrente criada com sucesso.")
    return conta

def main():
    LIMITE_TRANSACOES_DIARIAS = 10
    LIMITE_POR_SAQUE = 500

    while True:
        print("\n--- Sistema Bancário ---")
        print("1. Cadastrar Usuário")
        print("2. Criar Conta Corrente")
        print("3. Depositar")
        print("4. Sacar")
        print("5. Visualizar Extrato")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            cpf = input("Digite o CPF do usuário: ").replace(".", "").replace("-", "")
            usuario = next((u for u in usuarios if u["cpf"] == cpf), None)
            if usuario:
                criar_conta_corrente(usuario)
            else:
                print("Usuário não encontrado.")
        elif opcao == "3":
            numero_conta = int(input("Digite o número da conta: "))
            conta = next((c for c in contas if c["numero_conta"] == numero_conta), None)
            if conta:
                valor = float(input("Digite o valor a ser depositado: "))
                conta["saldo"], conta["extrato"] = depositar(conta["saldo"], valor, conta["extrato"])
            else:
                print("Conta não encontrada.")
        elif opcao == "4":
            numero_conta = int(input("Digite o número da conta: "))
            conta = next((c for c in contas if c["numero_conta"] == numero_conta), None)
            if conta:
                valor = float(input("Digite o valor a ser sacado: "))
                conta["saldo"], conta["extrato"] = sacar(
                    saldo=conta["saldo"], valor=valor, extrato=conta["extrato"],
                    limite=LIMITE_POR_SAQUE, numero_saques=conta["numero_saques"],
                    limite_saques=LIMITE_TRANSACOES_DIARIAS)
            else:
                print("Conta não encontrada.")
        elif opcao == "5":
            numero_conta = int(input("Digite o número da conta: "))
            conta = next((c for c in contas if c["numero_conta"] == numero_conta), None)
            if conta:
                visualizar_extrato(conta["saldo"], extrato=conta["extrato"])
            else:
                print("Conta não encontrada.")
        elif opcao == "6":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()