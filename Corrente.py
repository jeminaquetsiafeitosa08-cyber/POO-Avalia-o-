from contas.conta import Conta

class ContaCorrente(Conta):
    def sacar(self, valor):
        taxa = 2

        if valor <= 0:
            print("Valor inválido para saque.")
            return False

        if valor + taxa > self._saldo:
            print("Saldo insuficiente.")
            return False

        self._saldo -= (valor + taxa)
        self.historico.adicionar(f"Saque (corrente): -{valor} | Taxa: -{taxa}")
        return True


