estoque = []


#Função Adicionar produtos ao estoque

def adicionar_produto():
    nome_produto = input("Digite o nome de um produto:")
    estoque.append(nome_produto)

    quant_prod = int(input("Digite a quantidade do produto "))
    estoque.append(quant_prod)

# Função para verificar se um produto existe no estoque

def verifica_produto():
    for produto in estoque:
        if produto[0] == estoque:
            print("O produto", produto, " está em estoque ")
        else:
            print ("Não consta o produto em estoque")

def atualiza_produto():
    nova_quantidade = int(input("Digite a nova quantidade do produto:"))

    for produto[0] in estoque:



