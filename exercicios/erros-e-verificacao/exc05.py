# Controle de Estoque 

produtos = ["Chocolate", "Refrigerante", "Tomate", "Alface", "Macarrao", "Feijao", "Arroz"]

try:
    produto = input("Digite um produto: ")

    if produto in produtos:
        print("Esse produto está na lista.")

    if produto not in produtos:
        print("Produto não encontrado.")

except:
    print("Ocorreu um erro.")

