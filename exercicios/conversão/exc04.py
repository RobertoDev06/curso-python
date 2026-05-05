nome_produto = "Perfume"
quantidade = "20"
preco = "250"

quantidade = float(quantidade)
preco = float(preco)

retirada = int(input("Quantos produtos você deseja retirar: "))

quantidade_restante = quantidade - retirada
valor_retirado = preco * retirada

print("Quantidade retirada:", retirada)
print("Quantidade restante:", quantidade_restante)
print("Valor da retirada:", valor_retirado)