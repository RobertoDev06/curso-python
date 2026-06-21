# Investigando a Conversão

from decimal import Decimal

valor_conta = Decimal(100.00)
pessoas = Decimal(3)
valor_por_pessoa = valor_conta / pessoas
resultado = round(valor_por_pessoa, 2)
print(resultado)