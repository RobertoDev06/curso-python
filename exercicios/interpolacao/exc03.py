# Sistema Escolar

nome = input("Qual o seu nome: ")
nota1 = float ("Qual sua primeira nota: ")
nota2 = float ("Qual sua segunda nota: ")
nota3 = float ("Qual sua terceira nota: ")
nota4 = float ("Qual sua quarta nota: ")
media = (nota1 + nota2  + nota3 + nota4) / 4

print("%s ficou com a média de %2f" % (nome, media))