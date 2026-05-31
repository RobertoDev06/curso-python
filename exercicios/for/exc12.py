# Media de Nota

media = 0

for i in range(0,5):
    nota = float(input("Qual a sua nota: "))
    media = media + nota

mediaT = media / 5
print(f"O total da médias dos alunos: {mediaT}")