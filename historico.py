class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, valor):
        self.transacoes.append(valor)

    def __str__(self):
        return "\n".join([f"Transação: R$ {t:.2f}" for t in self.transacoes])
