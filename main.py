from sistema_bancario.pessoa_fisica import PessoaFisica
from sistema_bancario.conta_corrente import ContaCorrente
from sistema_bancario.transacao import Deposito, Saque

if __name__ == "__main__":
    cliente1 = PessoaFisica("Maria Silva", "123.456.789-00", date(1990, 5, 17))
    conta1 = ContaCorrente("0001", "1234", cliente1, limite=500.0)
    cliente1.adicionar_conta(conta1)

    conta1.depositar(1000)
    conta1.sacar(150)
    conta1.sacar(600)  # Testando limite
    conta1.depositar(200)

    print(conta1)
    print("Histórico de transações:")
    print(conta1.historico)
