# Sistema de Agendamento

horario = int(input("Qual horário deseja: "))

if horario == "":
    horario = None

if horario is None:
    print("Horário já preenchida por outro cliente.")

if horario is not None:
    print("Consulta agendada.")