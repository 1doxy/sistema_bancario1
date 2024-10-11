from .cliente import Cliente
from datetime import date

class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento):
        super().__init__(nome, cpf)
        self.data_nascimento = data_nascimento
