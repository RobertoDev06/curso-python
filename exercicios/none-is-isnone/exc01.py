# Cadastro de usuário

nome = input("Digite seu nome: ") # input() -> recebe dados do usuário

if nome == "": # if -> faz uma condição / == -> compara valores
    nome = None # None -> ausência de valor

# Verificando se é None
if nome is None: # is -> verifica identidade / is None -> verifica se está vazio
    print("Nenhum nome foi digitado.") # print() -> mostra mensagem na tela

# Verificando se NÃO é None
if nome is not None: # is not -> verifica se NÃO é / is not None -> verifica se tem valor
    print("Olá,", nome) # print() -> mostra mensagem na tela