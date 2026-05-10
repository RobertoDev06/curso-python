# Controle de Estoque

produto = input("Qual produto você deseja: ")

if produto == "":
    produto = None

if produto is None:
    print("Produto sem Cadastro.")

if produto is not None: 
    print("Produto Disponível.") 