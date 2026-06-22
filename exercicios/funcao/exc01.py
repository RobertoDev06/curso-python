# Pedido na Lanchonete

def Pedido():
    lanche = input("Qual lanche você deseja? ")
    bebida = input("Qual bebida você deseja? ")

    return lanche, bebida

    lanche, bebida = Pedido()

print(f"Lanche: {lanche}")
print(f"Bebida: {bebida}")
