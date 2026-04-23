from historico import Historico

class Conta:
    def __init__(self, cliente):
        self._saldo = 0
        self.cliente = cliente
        self.historico = Historico()

    def get_saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            self.historico.adicionar(f"Depósito: +{valor}")
            return True
        return False

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido.")
            return False

        if valor > self._saldo:
            print("Saldo insuficiente.")
            return False

        self._saldo -= valor
        self.historico.adicionar(f"Saque: -{valor}")
        return True
