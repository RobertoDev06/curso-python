# Ingresso

idade = int(input("Qual a sua idade: "))
ingresso = input("Você possui o ingresso do show [sim/nao]: ")

if idade >= 18 and ingresso == "sim":
    print("Entrada permitida")
elif idade >= 18 and ingresso == "nao":
    print("Comprar ingresso")
else:
    print("Entrada não permitida")