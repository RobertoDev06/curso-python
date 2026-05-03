# Exc01
idade = int(input('Qual sua idade: '))

if idade >= 18:
    print('Pode entrar!')
else:
    print('Não pode entrar!')
print()

# Exc02
compra = float(input('Qual foi o seu valor da compra: '))

if compra > 200:
    desconto = compra * 0.20
elif compra >= 100:
    desconto = compra * 0.10
else:
    desconto = 0

valor_final = compra - desconto

print(f'Desconto: R$ {desconto:.2f}')
print(f'Valor final: R$ {valor_final:.2f}')
print()

#Exc03
usuarioCerto = "paulo"
senhaCerto = "123"
usuario = input('Qual o nome do login: ')
senha = input('Qual a sua senha: ')

if usuario == usuarioCerto and senhaCerto == senha: 
    print('Acesso Aceito.')
else:
    print('Acesso Negado.')
print()


#Exc04 
valor = int(input('Digite um valor: '))
if (valor % 2 == 0) and valor > 10:
    valor = valor + 2
    print(valor)
elif (valor % 2 == 1) and valor < 5:
    valor = valor - 2
    print(valor)
else: 
    valor = 0
    print(valor)
print()

#Exc 05
salario = float(input('Qual o seu salario: '))
tempo = int(input('Quantas hora de trabalho: '))

if salario > 3000 and tempo >= 5:
    salario = salario + (salario * 0.15)
elif salario > 2000 or tempo >= 3:
    salario = salario + (salario * 0.10)
else:
    salario = salario + (salario * 0.5)
print(f'salario: R$ {salario}')
print()

#Exc 06
 
v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
v3 = int(input('Digite o terceiro valor: '))

if v1 > v2 and v3 < v1:
    v1 = v1 + 1
elif v1 < v2 or v3 == v1:
    v2 = v2 + 2
else:
    v3 = v3 + 3
print(v1)
print(v2)
print(v3)