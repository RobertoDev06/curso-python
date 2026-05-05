compra = float(input("Qual o valor da sua compra: "))

if compra < 100: 
    print("Sem desconto")
elif compra >= 100 and compra < 299:
    print("10% de desconto")
else:
    print("20% de desconto")