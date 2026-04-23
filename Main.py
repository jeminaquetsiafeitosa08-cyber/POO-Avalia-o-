     clientes.cliente import Cliente
from contas.corrente import ContaCorrente
from contas.poupanca import ContaPoupanca

contas = []


def criar_conta():
    nome = input("Nome do cliente: ")
    cpf = input("CPF: ")
    tipo = input("Tipo (1-Corrente / 2-Poupança): ")

    cliente = Cliente(nome, cpf)

    if tipo == "1":
        conta = ContaCorrente(cliente)
    elif tipo == "2":
        conta = ContaPoupanca(cliente)
    else:
        print("Tipo inválido!")
        return

    cliente.adicionar_conta(conta)
    contas.append(conta)

    print("Conta criada com sucesso!")


def escolher_conta():
    if not contas:
        print("Nenhuma conta cadastrada.")
        return None

    print("\nContas disponíveis:")
    for i, conta in enumerate(contas):
        print(f"{i} - {type(conta).__name__} | Cliente: {conta.cliente.nome}")

    try:
        indice = int(input("Escolha a conta: "))
        return contas[indice]
    except:
        print("Opção inválida.")
        return None


def menu():
    while True:
        print("\n1-Criar Conta\n2-Depositar\n3-Sacar\n4-Saldo\n5-Histórico\n0-Sair")
        op = input("Escolha: ")

        if op == "1":
            criar_conta()

        elif op == "2":
            conta = escolher_conta()
            if conta:
                try:
                    valor = float(input("Valor: "))
                    conta.depositar(valor)
                except:
                    print("Valor inválido.")

        elif op == "3":
            conta = escolher_conta()
            if conta:
                try:
                    valor = float(input("Valor: "))
                    conta.sacar(valor)
                except:
                    print("Valor inválido.")

        elif op == "4":
            conta = escolher_conta()
            if conta:
                print(f"Saldo: {conta.get_saldo()}")

        elif op == "5":
            conta = escolher_conta()
            if conta:
                conta.historico.mostrar()

        elif op == "0":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida.")


menu()
