from .conta import Conta

class ContaCorrente(Conta):
    def __init__(self, numero, agencia, cliente, limite):
        super().__init__(numero, agencia, cliente)
        self.limite = limite
        self.saques = 0

    def sacar(self, valor):
        if 0 < valor <= self.saldo + self.limite:
            self.saldo -= valor
            self.saques += 1
            self.historico.adicionar_transacao(-valor)
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            return True
        else:
            print("Saldo insuficiente ou valor inválido.")
            return False
