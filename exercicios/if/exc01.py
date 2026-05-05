idade = int(input("Qual a sua idade: "))

if idade <= 12: 
    print("Infantil")
elif idade >= 13 and idade <= 17:
    print("Adolescente")
else:
    print("Adulto")