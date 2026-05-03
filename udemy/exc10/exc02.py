# Introdução ao try/except

try:
    numero_str = input('Vou dobrar o número que vc digitar: ')
    
    numero_float = float(numero_str)
    print(f'O dobro de {numero_float} é {numero_float * 2}')

except:
    print('Isso não é um número')


numero = input('Vou dobrar o número que vc digitar: ')

try:
    print('STR:', numero)
    
    numero_float = float(numero)
    
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero} é {numero_float * 2}')
    
except:
    print('Isso não é um número')