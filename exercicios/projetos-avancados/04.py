# Sistema de Biblioteca
# Controlar com precisão o acervo de livros da instituição, sabendo instantaneamente quais volumes estão fisicamente disponíveis e quais foram retirados. 

# Continuae - olhar na ia onde estão os erros

biblioteca = {
    "É assim que acaba": True,
    "Kimetsu no Yaiba": True,
    "O Pequeno Príncipe": False,
    "1984": False,
    "Dandadan": True,
    "Wind Breaker": False,
    "Chainsaw": True
} 

def emprestar():
    livro = input("Digite o nome do livro: ")

    if livro in biblioteca:
        if biblioteca[livro] == True:
            biblioteca[livro] = False
            print(f"Emprestado: {livro}")
        else:
            print(f"Esse livro {livro} já está emprestado!")
    else:
        print("Livro não encontrado!")

def devolucao():
    livro = input("Digite o nome do livro: ")
    
    if livro in biblioteca:
        if biblioteca[livro] == False:
            biblioteca[livro] = True
            print(f"Feita a devolução do livro: {livro}")
        else:
            print("O livro já está disponível! ")
    else:
        print("Livro não encontrado!")        
    
def mostrarLivros():
    for livro, status in biblioteca.items():
        if status: # Mesma coisa que "status == True"
            print(f"{livro} - Disponível")
        else:
            print(f"{livro} - Emprestado")

while True:
    print("\n=== SISTEMA BIBLIOTECA ===")
    print ("1 - Emprestar")
    print ("2 - Devolução")
    print ("3 - Ver Livros")
    print ("4 - Sair")
    

    opcao = input("Qual opção você deseja: ")
    if opcao == "1":
        emprestar()
    elif opcao == "2":
        devolucao()
    elif opcao == "3":
        mostrarLivros()
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção Inválida!")

