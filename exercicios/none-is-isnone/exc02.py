# Sistema de Entrega

endereco = input("Qual o seu endereço: ")

if endereco == "":
    nome = None

if nome is None: 
    print("Nenhum nome foi digitado.")

if nome is not None:
    print("Seu endereço é: ", endereco)
