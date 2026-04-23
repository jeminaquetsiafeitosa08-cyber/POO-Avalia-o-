class Historico:
    def __init__(self):
        self._operacoes = []

    def adicionar(self, descricao):
        self._operacoes.append(descricao)

    def mostrar(self):
        for op in self._operacoes:
            print(op)

    def listar(self):
        return self._operacoes
