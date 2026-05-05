nota_teoria = float(input("Qual foi sua nota na teoria: "))
nota_pratica = float(input("Qual foi a sua nota na pratica: "))
presenca = float(input("Quanto de porcentagem você fez: "))

if (nota_pratica + nota_teoria) / 2 == 7 and presenca >= 75:
    print("Aprovado")
else: 
    print("Reprovado")