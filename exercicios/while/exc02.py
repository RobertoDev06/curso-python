# Contador de pessoas

contador = 0
resposta = "sim"

while resposta == "sim":
    pessoas = int(input("Quantas pessoas entrarão na festa: "))
    contador = contador + pessoas

    resposta = input("Deseja continuar? (sim/nao): ")

print("O total de pessoas que entrarão na festa foi:", contador)