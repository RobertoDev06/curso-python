# Operadores in e not in
#in -> dentro
#not in -> não está dentro

# Strings são iteráveis (podemos percorrer cada caractere)
# Índices:
#  0  1  2  3  4  5
#  O  t  á  v  i  o
# -6 -5 -4 -3 -2 -1

nome = 'Otávio'

# Verifica se a substring existe dentro da string
print('vio' in nome)   # True (existe em "Otávio")
print('zero' in nome)  # False (não existe)

# Apenas um separador visual
print(10 * '-')

# Verifica se NÃO existe dentro da string
print('vio' not in nome)   # False
print('zero' not in nome)  # True

# Pegando letras pelos índices
print(nome[0])   # O
print(nome[3])   # v

# Índices negativos (de trás pra frente)
print(nome[-1])  # o
print(nome[-3])  # v


nome = input('Digite seu nome: ')
# Pede o que o usuário quer encontrar dentro do nome
encontrar = input('Digite o que deseja encontrar: ')
# Verifica se o texto digitado está dentro do nome
if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
