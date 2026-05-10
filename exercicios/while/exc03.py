# Sistema de Notas
#Para quando digitar -1

soma = 0
quantidade = 0

nota = float(input("Qual foi sua nota: "))

while nota != -1:
    soma = soma + nota
    quantidade = quantidade + 1

    nota = float(input("Qual foi sua nota: "))

    media = soma / quantidade

print("Média final: ", media)