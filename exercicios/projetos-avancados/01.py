# Sistema de Controle de Estoque (Loja)

Estoque = []

while True:
    print("1 - Adicionar Produto: ")
    print("2 - Ver Estoque: ")
    print("3 - Sair")


    opcao = input("Esolhe uma das opções: ")

    if opcao == "1":
        try:
            nome = input("Qual Produto deseja: ")
            quantidade = int(input("Qual a quantidade do Produto: "))
            Estoque.append(nome, quantidade)
        except:
            print("Digite uma quantidade Válida")
    elif opcao == "2":
        for produto in Estoque:
            print(Estoque)
    elif opcao == "3":
        print("Programa encerrado")
        break
    else:
        print("Opção Inválido")
