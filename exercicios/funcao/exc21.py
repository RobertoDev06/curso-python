# Controle de Estoque 

def estoque():
    produtos = {
        "Limpeza": 10,
        "Comidas": 40,
        "Higiene": 25
    }

    for produto, quantidade in produtos.items():
        return "Produto:", produtos
        return "Quantidade: ",quantidade
    
        if quantidade < 10 or quantidade == 0:
            return "Repor  Estoque"
        else: 
            return "Estoque Ok"
        
print(estoque())