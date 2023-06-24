#Exercício 5: Remoção de duplicatas
#Escreva um programa que recebe uma lista de números do usuário e retorna a lista sem elementos #duplicados.***

numeros = input("Digite uma lista de números separados por espaço: ").split()
numeros = list(set(numeros))
print("A lista sem elementos duplicados é:", numeros)
