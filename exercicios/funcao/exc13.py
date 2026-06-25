# Controle de Entrada em um Evento

def Evento():
    while True:
        idade = int(input("Qual a sua idade: "))
        if idade < 0:
            return "Idade Inválida!"
        else:
            break
    ingresso = input("Possue o ingresso do evento (s/n): ")
    if idade >= 18 and ingresso == "s":
        return "Pode Entrar!"
    elif idade >= 18 and ingresso == "n":
        return "Não pode Enn=trar! Deve comprar o Ingresso"
    else:
        return "Menor de idade"
    
print(Evento())