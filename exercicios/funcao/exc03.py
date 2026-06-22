# Agendamento de Consulta

def Consulta(paciente, horario):
    return f"Paciente: {paciente}\nHorário: {horario}"

print(Consulta("Paulo Roberto", "18:00"))
print(Consulta(horario="17h", paciente="Francisco Roberto"))