# Funcionarios e Beneficio

def analisar():
    nomes = {
        "Paulo": 1000,
        "Luis": 2000,
        "Luisa": 3000,
        "Fernanda": 2000
    }

    for funcionario, salario in nomes.items():
        salario_final = salario + 300

        return "Nome: ", funcionario
        return "Salario: ", salario
        return "Salario Final: ",salario_final
        

        if salario > 1500 and salario < 4000:
            return "Beneficio aprovado"
        else:
            return "Beneficio Negado"
        
print(analisar())