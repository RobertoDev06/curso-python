# Sistema de Cadastro de Funcionários

funcionarios = []

def Cadastro():
    nome = input("Qual seu nome completo: ").strip().upper()
    idade = int(input("Qual a sua idade: ").strip())
    salario = float(input("Qual a sua renda salarial: ").strip())
    cargo = input("Qual o seu cargo: ").strip().upper()
    setor = input("Qual o seu setor: ").strip().upper()

    funcionario = { ## DICIONARIO
    "nome": nome,
    "idade": idade,
    "salario": salario,
    "cargo": cargo,
    "setor": setor
    }
    funcionarios.append(funcionario) #v VIRA LISTA

def Listagem():
    for index, funcionario in enumerate(funcionarios): #VAI PEGAR OS VALORES DO DICIONARIIO
        index += 1
        print(f"ID: {index}")
        print(f"Nome: {funcionario['nome']}")
        print(f"Idade: {funcionario['idade']}")
        print(f"Salario: {funcionario['salario']}")
        print(f"Cargo: {funcionario['cargo']}")
        print(f"Setor: {funcionario['setor']}")

Cadastro()
Listagem()
