# Velocidade

velocidade = int(input("Qual a sua velocidade: "))

if velocidade < 40:
    print("Velocidade baixa.")
elif velocidade < 80:
    print("Velocidade normal.")
elif velocidade < 120:
    print("Velocidade alta")
else:
    print("Velocidade muito alta")