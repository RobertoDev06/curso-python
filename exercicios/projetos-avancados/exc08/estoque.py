estoque = [
    {
        "Produto": "Copo",
        "Preço": 5.00,
        "Quantidade": 50
    },
    {
        "Produto": "Prato",
        "Preço": 12.00,
        "Quantidade": 30
    },
    {
        "Produto": "Colher",
        "Preço": 3.50,
        "Quantidade": 100
    },
    {
        "Produto": "Garfo",
        "Preço": 4.00,
        "Quantidade": 80
    },

]

def Procurar(nome):
    for produto in estoque: # O produto irá pegar cada bloco (os {}) do dicionario 
        if nome == produto["Produto"]: # Nessa parte ele irá olha cada nome do produto que estão em cada bloco (os {})
            return nome
    return "Não achamos esse produto no nosso estoque!"

digite = input("Qual produto você deseja? ")
print(Procurar(digite))