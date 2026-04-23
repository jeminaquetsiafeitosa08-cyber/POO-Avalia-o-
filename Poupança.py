from contas.conta import Conta

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido para saque.")
            return False

        if valor > self._saldo:
            print("Saldo insuficiente.")
            return False

        self._saldo -= valor
        self.historico.adicionar(f"Saque (poupança): -{valor}")
        return True
