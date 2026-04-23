class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def listar_contas(self):
        for conta in self.contas:
            print(f"{type(conta).__name__} - Saldo: {conta.get_saldo()}")

    def mostrar_extratos(self):
        for conta in self.contas:
            print(f"\nExtrato da {type(conta).__name__}:")
            conta.historico.mostrar()
