# Prcelamento de Celular

preco = 2.400
juros = 8 # Por mes

parcela = float(input("Quantas parcelas você deseja: "))

valor_juros = preco * (juros / 100)
total = preco + valor_juros

valor_parcela = total / parcela

print("O valor total com juros e as parcelas", total)
print("O total do celular parcelado: ", valor_parcela)