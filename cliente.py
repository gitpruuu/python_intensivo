from pessoa import Pessoa
from conta_corrente import Conta


class Cliente(Pessoa):

    def __init__(
            self, primeiro_nome,
            ultimo_nome, idade,
            telefone, email, agencia,
            numero_da_conta
    ):
        super().__init__(primeiro_nome, ultimo_nome, idade, telefone, email)
        self.conta_corrente = Conta(agencia, numero_da_conta)
