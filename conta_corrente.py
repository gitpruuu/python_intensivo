import conta_corrente
import cliente


class Conta():

    def __init__(self, agencia, numero_da_conta):
        self.agencia = agencia
        self.numero_da_conta = numero_da_conta
        self.titular = "Vazio"
        self.saldo = 1000

    def tirar_extrato(self):
        print("Saldo atual R$: " + str(self.saldo))

    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                valor_sacado = valor
                print("Sacou R$: "+str(valor))
            else:
                print("Saldo suficiente.")
        else:
            print("Informe um valor válido.")
        return valor_sacado

    def tranferir(self, valor, conta_destino):
        if valor > 10:
            if self.saldo >= valor:
                self.saldo -= valor
                conta_destino.saldo += valor
            else:
                print("Saldo suficiente.")
        else:
            print("Quantia mínima para transferencia é de R$ 10!")

    def depositar(self, valor):
        if valor > 10:
            self.saldo += valor
            print("Deposito de R$:" + str(valor) + " realizado.")
        else:
            print("valor mínimo para depósito é de R$ 10!")

    def mostrar_detalhes(self):
        detalhes = "Titular: "+self.titular.primeiro_nome.title() +\
            "\nAgencia: " + str(self.agencia) + \
            "\nNumero da conta: " + str(self.numero_da_conta) + \
            "\nSaldo disponivel: " + str(self.saldo)
        print("Detalhes da conta")
        print(detalhes)
