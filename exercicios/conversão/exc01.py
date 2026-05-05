arroz = "5.50"
feijao = "7.30"
carne = "25.90"

print("Preço do arroz: " + arroz)
print("Preço do feijao: " + feijao)
print("Preço da carne: " + carne)

arroz = float(arroz)
feijao = float(feijao)
carne = float(carne)

total = arroz + feijao + carne


print(f"Total da compra: R$ {total:.2f}")