# Controle de Acesso

tentativas = 0

while tentativas < 3:
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario == "admin" and senha == "1234":
        print("Login realizado com sucesso!")
        break
    else:
        tentativas += 1
        print("Usuário ou senha incorretos.")

if tentativas == 3:
    print("Conta bloqueada")