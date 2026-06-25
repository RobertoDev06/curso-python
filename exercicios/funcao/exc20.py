# Situação dos Alunos

def alunos():
    nomes ={
        "Paulo": 10,
        "Calebe": 8 ,
        "Maria": 9
    }

    for nome, nota in nomes.items():
        return "Aluno", nome
        return "Nota: ", nota
        if nota >= 7:
            return "Aprovado"
        else:
            return "Reprovado"