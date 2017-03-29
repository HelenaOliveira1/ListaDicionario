# QUESTÃO 3

produtos = {}

def cadastrarProduto(produtos, produto, preco):
    produtos[produto] = preco
    print(produtos)

    return produtos

def exibirProdutos(produtos):
    print("Lista de Produtos: \n", produtos, "\n")

def removerProduto (produtos, produto):
    if (produto in produtos):
        produtos.pop(produto)
        print(produtos)
    else:
        print("PRODUTO NÃO CADASTRADO!")
        
    return produtos

def exibirCaroProduto(produtos):
    precos = produtos.values()
    for p in produtos:
        if (produtos[p] == max(precos)):
            print("Produto mais caro: ",p, ":", max(precos))

    return precos

def exibirBaratoProduto(produtos):
    precos = produtos.values()
    for p in produtos:
        if (produtos[p] == min(precos)):
            print("Produto mais barato: ",p,":", min(precos))

    return precos

def main(Args=None):
    cont = "s"
    while (cont == 's'):
        op = int(input("O que deseja?\n1. Cadastrar Produto.\n2. Exibir Produtos.\n3. Remover Produto.\n4. Exibir Produto mais caro.\n5. Exibir Produto mais barato.\n6. sair.\n"))
        if (op == 1):
            produto = str(input("Digite o nome do produto para cadastrar: "))
            preco = float(input("Digite o preço do produto para cadastrar: "))
            cadastrarProduto(produtos, produto, preco)
        elif (op == 2):
            exibirProdutos(produtos)
        elif (op == 3):
            produto = str(input("Digite o produto que você deseja remover: "))
            removerProduto(produtos, produto)
        elif (op == 4):
            exibirCaroProduto(produtos)
        elif (op == 5):
            exibirBaratoProduto(produtos)
        elif (op == 6):
            cont = "n"
            print("OBRIGADO!")
        else:
            print("OPÇÃO INVÁLIDA!!")
            
if(__name__ == __name__):
  main()


        
        
