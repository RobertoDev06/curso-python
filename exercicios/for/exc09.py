# Controle de Turmas

nota = 0
contagem = 0
soma = 0 

alunos = int(input("Quantos alunos: "))

for i in range(alunos):
    nota = float(input("Qual a sua nota: "))
    if nota >= 7:
        contagem = contagem + 1
        soma = soma + nota

print(f"A quantidade de alunos aprovados: {contagem}")
print(f"A soma total das notas do alunos aprovados: {soma}")

