# Sistema de Compras

def Compra():
    total = 0
    while True:
        preco = float(input("Qual o valor da compra (0 para sair): "))
        if preco ==0:
            break
        total += preco
        if preco > 500:
            total = total - (total * 0.10)
        elif preco > 300:
            total = total - (total * 0.0)
        else:
            return "Zero desconto"
    return "O total das compras foi de : " + total

print(Compra())
