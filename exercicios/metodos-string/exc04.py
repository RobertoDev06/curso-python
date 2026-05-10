# Cadastro de Produtos 

frase = input("Faça sua lista de compras (que utilize virgulas para separar os produtos): ")
produtos = frase.split(",")

print("\nProdutos cadastrados: ")

for produto in produtos:
    print(produto.strip())