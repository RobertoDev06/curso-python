# Sistema de Agenda Inteligente

Caixa = []

clientes = int(input("Quantos cliente temos hoje? ")) # Usei para adicionar varios dados.


# Terminar 
# Usar o set 

i = 0 
while i < clientes:
    nome = input("Qual o seu nome: ")
    cpf = input("Qual o seu cpf: ")
    telefone = input("Qual o seu telefone: ")
    DadosClientes = {
            "nome": nome,
            "cpf": cpf, 
            "telefone": telefone
    }
    if cpf == DadosClientes["cpf"] and telefone == DadosClientes["telefone"]:
        print("Cliente já Cadastrado!")
    else: 
        Caixa.append(DadosClientes)
        print(Caixa)
    i += 1