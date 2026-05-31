# Sistema de Mensagens 

mensagens = [
    ["Olá, bom dia", True],
    ["Tudo bem?", False],
    ["Você é fera", False],
    ["Parabéns", True],
    ["Show! Se garantiu", True]
]

for mensagem in mensagens:
    if mensagem[1] == True:
        print(mensagem[0])