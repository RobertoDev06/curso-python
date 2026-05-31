# Desconto

compra = float(input("Qual o valor da sua compra: "))
desconto = input("Possue cupom da loja: ")

if compra > 200 or desconto == "sim":
    print("Ganhou um cupom!")
else:
    print("Não ganhou um cupom!")