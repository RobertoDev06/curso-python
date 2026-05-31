# Cofre Digital

senha = "1234"
erro = 0

for i in range(5):
    digite = input("Qual a senha: ")

    if digite == senha:
        print("Cofre Desbloqueado")
        break

    erro += 1

if erro == 5:
    print("Acesso Bloqueado")

print(f"O total de tentativas incorretas foi de: {erro}")