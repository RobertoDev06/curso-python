# Caixa Eletrônico

saldo = 1000

while True:
    print("\n=== CAIXA ELETRÔNICO ===")
    print("1 - Sacar")
    print("2 - Consultar saldo")
    print("3 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        valor = float(input("Digite o valor do saque: "))

        if valor > 0 and valor <= saldo:
            saldo -= valor
            print(f"Saque realizado com sucesso!")
            print(f"Saldo atual: R${saldo:.2f}")
        else:
            print("Saque inválido.")

    elif opcao == 2:
        print(f"Saldo disponível: R${saldo:.2f}")

    elif opcao == 3:
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")