# Controle de Senha

def Login(usuario, senha):
    while usuario == "adm" and senha == "1234":
        usuario = input("Qual o nome do ususario: ")
        senha = input("Qual a senha: ")

        if usuario == "adm" and senha == "1234":
            return "Acesso Liberado"
        else:
            return "Acesso Negado"
        
print(Login())
    