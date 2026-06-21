# Checando o Tipo do Preço

from decimal import Decimal

preço = "19.90"
preço = Decimal('19.90')
resultado = preço
print(resultado)
print(type(resultado))