estoque = []  # lista para armazenar o estoque de produtos

def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade em estoque: "))
    
    produto = [nome, quantidade]
    estoque.append(produto)
    print("Produto adicionado ao estoque.")

def remover_produto():
    nome = input("Digite o nome do produto: ")
    
    for produto in estoque:
        if produto[0] == nome:
            estoque.remove(produto)
            print("Produto removido do estoque.")
            return
    
    print("Produto não encontrado.")

def atualizar_estoque():
    nome = input("Digite o nome do produto: ")
    
    for produto in estoque:
        if produto[0] == nome:
            quantidade = int(input("Digite a nova quantidade em estoque: "))
            produto[1] = quantidade
            print("Estoque atualizado.")
            return
    
    print("Produto não encontrado.")

def exibir_estoque():
    print("--- Estoque de Produtos ---")
    
    for produto in estoque:
        nome, quantidade = produto
        print(f"{nome}: {quantidade}")
    
    print("--------------------------")

def menu():
    print("===== Controle de Estoque =====")
    print("1. Adicionar Produto")
    print("2. Remover Produto")
    print("3. Atualizar Estoque")
    print("4. Exibir Estoque")
    print("0. Sair")
    print("==============================")

    opcao = input("Digite a opção desejada: ")
    print()

    if opcao == "1":
        adicionar_produto()
    elif opcao == "2":
        remover_produto()
    elif opcao == "3":
        atualizar_estoque()
    elif opcao == "4":
        exibir_estoque()
    elif opcao == "0":
        print("Programa encerrado.")
        return
    else:
        print("Opção inválida.")

    print()
    menu()

menu()


