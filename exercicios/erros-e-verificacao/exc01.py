# Login Simples

usuarios = ["João", "Maria", "Carlos", "Artur"]
nome = input("Qual o seu nome: ")

if nome in usuarios: 
    print("Usuário encontrado.")

if nome not in usuarios: 
    print("Usuário não cadastrado.")