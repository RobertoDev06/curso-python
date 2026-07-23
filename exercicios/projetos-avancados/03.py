# Sistema Bancário
# Simular rotinas transacionais de depósito, saque e consulta de saldo de forma segura, bloqueando inconsistências graves como saques descobertos ou sem saldo.

# Fazer mais exercicios como esses

saldo = 0.0
extrato = []
def deposito():
    global saldo
    valor = float(input("Digite o valor do depósito: "))

    if valor > 0 and valor <= saldo:
        saldo += valor
        extrato.append(f"Deposito: R${valor:.2f}")
        print("Deposito realizado com sucesso!")
    else:
        print("Nenhum Deposito.")

def saque():
    global saldo

    valor = float(input("Digite o valor do depósito: "))

    if valor > 0 and valor <= saldo:
        saldo -= valor
        extrato.append(f"Saque: R${valor:2f}")
        print("Saque realizado com sucesso!")
    else: 
        print("Saque não realizado.")

def ConsultarSaldo():
    print(f"Seu saldo atual está: {saldo:.2f}")

def MostrarExtrato():
    print("\n=== EXTRATO ===")

    if len(extrato) == 0:
        for i in extrato:
            print(f"Seu Extrato: {i}")
    print(f"Seu saldo atual está: {saldo:.2}")

while True: 
    print("\n=== SISTEMA BANCÁRIO ===")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Consultar Saldo")
    print("4 - Extrato")
    print("5 - Sair")

    opcao = input("Qual opção você Irá escolhe: ")
    if opcao == "1":
        deposito()
    elif opcao == "2":
        saque()
    elif opcao == "3":
        ConsultarSaldo()
    elif opcao == "4":
        MostrarExtrato()
    else:
        print("Solicitou a saída do banco!")

