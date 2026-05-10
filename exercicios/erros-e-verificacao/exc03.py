# Caixa Eletrônico

try:  # tenta executar
    saque = float(input("Digite o valor do saque: "))
    print("Saque de %.2f realizado." % saque)

except: # executa se acontecer um erro 
    print("Valor inválido.")

