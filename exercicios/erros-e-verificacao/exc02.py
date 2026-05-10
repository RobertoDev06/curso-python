# Lista de Convidados 

convidados = ["Paulo", "Suiane", "Maria", "Felipe", "Artur", "Sabrina", "Ana"]
nome = input("Qual o seu nome: ")

if nome in convidados: 
    print("Pode entrar.")

if nome not in convidados:
    print("Não pode entrar.")