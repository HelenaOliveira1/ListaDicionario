#QUESTÃO 1

dias = {}

def adicionarDia(posicao, dia):
    if(posicao >= 1 or posicao <= 7):
        dias[posicao] = dia
        print(dias)
    else:
        print("A semana tem apenas 7 dias!")
    
    return dias

def exibirDias(dias):
    for d in dias:
        print("Dia: ", d,"\n")


def main(Args=None):
    cont = "s"
    while (cont == 's'):
        op = int(input("O que deseja?\n1. Adicionar dia à semana.\n2. Exibir dias da semana.\n3. Sair.\n"))
        if (op == 1):
            posicao = int(input("Digite um número para a posição: "))
            dia = str(input("Digite o dia da semana para ser adicionado: "))
            adicionarDia(posicao, dia)
        elif (op == 2):
            exibirDias(dias)
        elif (op == 3):
            cont = "n"
            print("OBRIGADO!")
        else:
            print("OPÇÃO INVÁLIDA!!")
            
if(__name__ == __name__):
  main()
