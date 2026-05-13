# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

# Exemplo de desempacotamento que estava comentado:
# p, b, *_, ap, u = lista
# print(p, u, ap)

# Para imprimir a lista desempacotada (como o instrutor sugere):
print(*lista)
print(*string)
print(*tupla)