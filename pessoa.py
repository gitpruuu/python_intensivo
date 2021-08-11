class Pessoa():

    def __init__(self, primeiro_nome, ultimo_nome, idade, telefone, email):
        self.primeiro_nome = primeiro_nome
        self.ultimo_nome = ultimo_nome
        self.idade = idade
        self.telefone = telefone
        self.email = email

    def alterar_email(self, novo_email):
        if novo_email != "":
            if "@" in novo_email:
                self.email = novo_email
            else:
                print("Informe um e-mail válido.")
        else:
            print("E-mail não pode ser vazio!")

    def alterar_telefone(self, novo_telefone):
        if novo_telefone != "":
            self.telefone = novo_telefone
        else:
            print("Informe um telefone válido.")

    def exibir_detalhes(self):
        detalhes = "Nome: " + str(self.primeiro_nome) +\
            "\nSobrenome: " + str(self.ultimo_nome) +\
            "\nIdade: " + str(self.idade) +\
            "\nTelefone: " + str(self.telefone) +\
            "\nE-mail:" + str(self.email)
        print("Detalhes")
        print(detalhes)
