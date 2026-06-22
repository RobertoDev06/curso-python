# Cadastro de Aluno

def cadastrarAluno(nome, curso):
    return f"Nome: {nome}\nCurso: {curso}"

# Argumentos posicionais
print(cadastrarAluno("Paulo", "Python"))

# Argumentos nomeados
print(cadastrarAluno(nome="Maria", curso="Informática"))