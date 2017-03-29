#QUESTÃO 2

funcionarios = {}

def adicionarFuncionario(matricula, nome):
    if (matricula in funcionarios):
        print("MATRÍCULA JÁ CADASTRADA!")
    else:
        funcionarios[matricula] = nome
        print(funcionarios)

    return funcionarios
    
def buscarFuncionario(matricula):
    if (matricula in funcionarios):
        print("Funcionário: ", funcionarios[matricula])
    else:
        print("MATRÍCULA NÃO CADASTRADA!")
        
def exibirFuncionario(funcionarios):
    for f in funcionarios:
        print("Funcionário (matrícula): ", f, "\n")
        
def main(Args=None):
    cont = "s"
    while (cont == 's'):
        op = int(input("O que deseja?\n1. Adicionar funcionário.\n2. Buscar funcionário.\n3. Exibir funcionários.\n4. Sair.\n"))
        if (op == 1):
            matricula = int(input("Digite a matrícula do funcionário: "))
            nome = str(input("Digite o nome completo do seu funcionário: "))
            adicionarFuncionario(matricula, nome)
        elif (op == 2):
            matricula = int(input("Digite a matrícula do funcionário: "))
            buscarFuncionario(matricula)
        elif (op == 3):
            exibirFuncionario(funcionarios)
        elif (op == 4):
            cont = "n"
            print("OBRIGADO!")
        else:
            print("OPÇÃO INVÁLIDA!!")
            
if(__name__ == __name__):
    main()

