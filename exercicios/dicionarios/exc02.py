# Dicionário
pessoa = {
    "nome": "Maria",
    "idade": 20
}

# len() -> Conta quantas chaves existem
print(len(pessoa))
# 2

# keys() -> Mostra as chaves
print(pessoa.keys())
# dict_keys(['nome', 'idade'])

# values() -> Mostra os valores
print(pessoa.values())
# dict_values(['Maria', 20])

# items() -> Mostra chave e valor
print(pessoa.items())
# dict_items([('nome', 'Maria'), ('idade', 20)])

# setdefault() -> Adiciona uma chave se ela não existir
pessoa.setdefault("cidade", "Fortaleza")
print(pessoa)
# {'nome': 'Maria', 'idade': 20, 'cidade': 'Fortaleza'}

# copy() -> Cria uma cópia do dicionário
copia = pessoa.copy()
print(copia)

# get() -> Busca um valor sem gerar erro
print(pessoa.get("nome"))
# Maria

print(pessoa.get("telefone"))
# None

# pop() -> Remove uma chave e retorna o valor
idade = pessoa.pop("idade")
print(idade)
# 20

print(pessoa)
# {'nome': 'Maria', 'cidade': 'Fortaleza'}

# popitem() -> Remove o último item
ultimo = pessoa.popitem()
print(ultimo)
# ('cidade', 'Fortaleza')

print(pessoa)
# {'nome': 'Maria'}

# update() -> Adiciona ou atualiza dados
pessoa.update({
    "idade": 21,
    "cidade": "São Paulo"
})

print(pessoa)
# {'nome': 'Maria', 'idade': 21, 'cidade': 'São Paulo'}