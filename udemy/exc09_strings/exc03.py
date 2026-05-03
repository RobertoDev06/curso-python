# Alinhamento e preenchimento com f-strings

# >  -> alinha à direita
# <  -> alinha à esquerda
# ^  -> centraliza

variavel = 'ABC'

# Sem formatação
print(f'{variavel}')

# Alinhado à direita em 10 caracteres
print(f'{variavel: >10}')  

# Alinhado à esquerda em 10 caracteres
print(f'{variavel: <10}')

# Centralizado em 10 caracteres
print(f'{variavel: ^10}')

# Centralizado com preenchimento usando $
print(f'{variavel: $^10}')

print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')