# Sistema de Vendas (Frente de Caixa)

Carrinho = []

resposta = int(input("Quantas compras irá fazer? "))

i = 0 

while i < resposta:
    nome = input("Qual o nome do produto: ")
    preco = float(input("Qual o preço do produto"))

    Produto = {
        "nome":  nome,
        "preco": preco
    }

    Carrinho.append(Produto)
    i += 1; 

total = sum([produto["preco"] for produto in Carrinho])
print(total)

if total >= 8000:
    desconto = 0.40
elif total >= 4000:
    desconto = 0.30
else:
    desconto = 0.15

Valordesconto = lambda total: total - (total * desconto)
ValorFinal = Valordesconto(total)

print(f"Total da compra: R${total:.2f}")
print(f"Valor com desconto: R$ {ValorFinal:.2f}")
