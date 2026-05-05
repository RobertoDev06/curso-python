# Conta de luz
consumo_kwh = 250
tarifa = 0.80
bandeira = 2

valor_base = consumo_kwh * tarifa


if bandeira == 1:
    valor_final = valor_base + (valor_base * 0)
elif bandeira == 2:
    valor_final = valor_base + (valor_base * 0.10)
else:
    valor_final = valor_base + (valor_base * 0.25)

print(f"Valor base: R$ {valor_base:.2f}")
print(f"Valor final da conta: R$ {valor_final:.2f}")