# Sistema de Academia

def Academia():
    while True:
        idade = int(input("Qual a idade do aluno: "))
        atestado = input("Possue o atestado médico: ")
        if idade >= 16 and atestado == "sim":
            return "Treino Liberado!"
        elif idade >= 16 or atestado == "sim":
            return "Precisa de Autorização!"
        else:
            return "Treino não Permitido!"
        
print(Academia())