class Banco():

    def __init__(self, nome_do_banco):
        self.nome_do_banco = nome_do_banco
        self.funcionarios = []
        self.clientes = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def exibir_funcionario(self):
        for funcionario in self.funcionarios:
            print(funcionario)

    def exibir_clientes(self):
        for cliente in self.clientes:
            print(cliente)
