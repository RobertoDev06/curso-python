# Sistema de Analise de Dados

Dados = [150.60, 100, 30, 65, 900, 1220, 400, 23, 300, 504, 23, 700, 439, 800]
i = 0
media = 0

sum(Dados) # Soma tudo
len(Dados) # Irá contar quantos dados tem na List
media = sum(Dados) / len(Dados)

print(f"O maior faturamento da Analise foi de: {max(Dados)}")
print(f"O pior dia de venda foi no valor de: {min(Dados)}")
print(f"A média dos valores foi de: {media}")