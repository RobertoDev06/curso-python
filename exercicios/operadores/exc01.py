# Supermercado (Desconto + Imposto)

produto = 120.00
desconto = 20
imposto = 10

print("O valor do produto é de: ", produto)
print(f"Você ganhou um desconto de: {desconto}%")

valor = (produto - (produto * desconto / 100)) + imposto

print("Seu valor da compra foi: ", valor)