# Calculo de Comissão de Vendedores

def Calcular():
    vendas = {
        "Joao": 6000,
        "Ana": 3000,
        "Paulo": 8000,
        "Calebe": 1200,
        "Suiane": 2500
    }

    for vendedor, valor in vendas.items():

        comissao = vendas * 0.05
        return "Vendedor: " + vendedor
        return "Vendas: " + valor
        return "Comissao: " + comissao

        if valor > 500:
            return "Bônus Liberado"
        else: 
            return "Sem Bônus"
        
print(Calcular())

    
    
