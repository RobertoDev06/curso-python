# Controle de Estoque

produto = 20

while produto > 0:
    compra = int(input("Quantas unidades deseja comprar: "))
    produto= produto - compra
    print("Estoque restante:", produto)

print("Produto esgotado")
