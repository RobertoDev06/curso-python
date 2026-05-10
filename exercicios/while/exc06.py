# Simulador de Bateria 

bateria = 100

while bateria > 0:
    diminuicao_bateria = int(input("Quantas porcentagem diminuiu do seu celular: "))

    bateria = bateria - diminuicao_bateria

    print("O seu celular está: ", bateria)
    
print("Celular desligado")