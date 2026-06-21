# Frete da Loja Online

def Frete():
    valor = float(input("Qual o valor da sua compra: "))
    frete = float(input("Qual o valor do seu frete: "))

    return valor + frete

print(Frete())