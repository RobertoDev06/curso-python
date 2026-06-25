# Controle de Gastos Mensais

def Analisar(gastos):
    for despesa, valor in gastos.items():
        if valor > 200 and valor < 1000:
            print(despesa, "- Gasto Moderado")
        else:
            print(despesa, "- Fora do Padrão")
            
gastos = {
    "aluguel": 800,
    "mercado": 300,
    "internet": 120,
    "luz": 90
}

Analisar(gastos)