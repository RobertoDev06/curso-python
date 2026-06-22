# Reserva de Hotel

def Reserva():
    cliente = input("Qual o seu nome: ")
    horario = input("Qual o horário: ")

    return cliente, horario

cliente, horario = Reserva()
print(cliente)
print(horario)