# QUESTÃO 4

turmas = {}

def adicionarAlunoNotas():
    nomeTurma = str(input("Digite o nome da turma do aluno: "))
    if (nomeTurma in turmas):
        print("Turma: ", turmas[nomeTurma])
        alunos = {}
        matricula = str(input("Digite a matrícula do aluno: "))
        notas = []
        mais = "s"
        while(mais == "s"):
            nota = float(input("Digite a nota: "))
            notas.append(nota)
            mais = str(input("Se houver mais notas, digite s, senão, digite n: "))
        turmas[nomeTurma][matricula] = notas
        print("Turma: ", turmas[nomeTurma])
    else:
        print("TURMA NÃO CADASTRADA")

def adicionarTurma():
    nome = str(input("Digite o nome da turma para ser adicionado: "))
    alunos = {}
    turmas[nome] = alunos
    print("Turmas:", turmas)

def calcularMedia(notas):
    soma = 0
    for n in notas:
        soma += n
        media = soma/len(notas)
        
    return media

def mediaTurma():
    soma = 0
    cont = 0
    nomeTurma = str(input("Digite o nome da turma: "))
    if (nomeTurma in turmas):
        for t in turmas[nomeTurma]:
            soma += calcularMedia(turmas[nomeTurma][t])
            cont += 1
        media = soma/cont
        print("Média: ",media)
    else:
        print("TURMA NÃO CADASTRADA")
        
    return 

def main():
    cont = 1
    while (cont > 0):
        op = int(input("\nMENU\n1. Adicionar Turma\n2. Adicionar Aluno e Notas\n3. Calcular média de um Aluno\n4. Calcular média de uma Turma.\n5. Sair\n"))
        if (op == 1):
            adicionarTurma()
        elif (op == 2):
            adicionarAlunoNotas()
        elif (op == 3):
                turma = str(input("Digite a turma: "))
                if (turma in turmas):
                    matricula = str(input("Digite a matricula: "))
                    if (matricula in turmas[turma]):
                        print("Média: ", calcularMedia(turmas[turma][matricula]))
                    else:
                        print("MATRÍCULA NÃO CADASTRADA")
                else:
                    print("TURMA NÃO CADASTRADA")
                    
        elif (op == 4):
            mediaTurma()
        elif (op == 5):
            print("OBRIGADO!!")
            cont = 0
        else:
            print("OPÇÃO INVÁLIDA")

if (__name__ == "__main__"):
    main()
    

