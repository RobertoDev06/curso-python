# Calculadora de Salario

def Salario():
    while True: 
        salario = float(input("Qual o seu salario: "))
        if salario == 0: 
            break
        if salario >= 200:
            salario = salario + (salario * 0.15)
            return "Seu saldo atual é de: " + salario
        elif salario >= 5000:
            salario = salario + (salario * 0.10)
            return "Seu saldo atual é de: " + salario
        else: 
            salario = salario + (salario * 0.05)
            return "Seu saldo atual é de: " + salario
        
    
        