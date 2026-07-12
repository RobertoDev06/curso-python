# Criando um dicionário vazio
pessoa = {}

# Adicionando dados
pessoa["nome"] = "Luiz Otávio"
pessoa["sobrenome"] = "Miranda"

print(pessoa)
# {'nome': 'Luiz Otávio', 'sobrenome': 'Miranda'}

# Alterando um valor
pessoa["nome"] = "Maria"

print(pessoa)
# {'nome': 'Maria', 'sobrenome': 'Miranda'}

# Removendo um item
del pessoa["sobrenome"]

print(pessoa)
# {'nome': 'Maria'}