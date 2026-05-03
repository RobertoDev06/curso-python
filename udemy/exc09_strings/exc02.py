"""
Interpolação básica de strings

%s -> string
%d ou %i -> números inteiros
%f -> números com ponto flutuante (float)
%x ou %X -> hexadecimal
"""

# Variáveis
nome = 'Luiz'
preco = 1000.95897643
idade = 25
numero = 255

# Formatação:
# %.2f significa: 2 casas decimais
variavel = '%s, o preço é R$%.2f' % (nome, preco)

# Exibe o resultado formatado
print(variavel)

# String + inteiro + float + hexadecimal
texto = '%s tem %d anos e o preço é R$%.2f' % (nome, idade, preco)
print(texto)

# Hexadecimal (minúsculo e maiúsculo)
print('Número em hexadecimal: %x' % numero)  # ff
print('Número em hexadecimal: %X' % numero)  # FF