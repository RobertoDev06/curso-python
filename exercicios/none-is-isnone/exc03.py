# Login Simples

usuario = input("Qual seu nome: ")
senha = int(input("Qual a sua senha: "))

if senha == "":
    senha = None

if senha is None: 
    print("Senha inválida.")

if senha is not None:
    print("Login realizado.")