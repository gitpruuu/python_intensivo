from cliente import Cliente

c1 = Cliente(
    "Fernanda", "Apolly", 45, "(11)9448-10177",
    "apolly@gmail.com", 9417, "1340-1"
)
c2 = Cliente(
    "Gabriel", "Albert", 72, "(11)9884-45677",
    "giel.bert@gmail.com", 9417, "1341-1"
)

c1.conta.mostrar_detalhes()
c1.conta.tranferir(500, c2.conta)
c2.conta.mostrar_detalhes()
