# Estoque

caixa = 0
soma = 0
contagem = 0

print(f"O seu caixa está com esse valor inicial: {caixa}")
vendasQ = int(input("Quantas vendas deseja: "))

for i in range(vendasQ):
    compra = float(input("Qual o valor da sua compra: "))
    caixa = caixa + compra
    contagem = contagem + 1
    
print(f"O total da sua caixa final foi de: {caixa}")
print(f"A quantidade de produtos vendidos foi de: {contagem}")