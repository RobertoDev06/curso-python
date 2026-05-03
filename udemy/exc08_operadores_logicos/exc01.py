# AND (e)
entrada = input('[E]entrar ou [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar!')
else:
    print ("Sair!")

print (True and False and True) #Para no False

print()

#OR (ou)
entrada = input('[E]entrar ou [S]air: ')
senha_digitada = input('Senha: ')
senha = '123'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha:
    print('Entrar!')
else:
    print("Sair!")

print (True or False or False)

print()

#NOT (não)
#True -> False
#False -> True

senhas = input('Senha: ')

if senhas != '12345':
    print('Entrou')
else:
    print('Senha incorreta')

print(not True)   # False
print(not False)  # True