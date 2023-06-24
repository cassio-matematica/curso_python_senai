##Exercício 4: Inversão da lista
#Escreva um programa que recebe uma lista de elementos do usuário e retorna a lista invertida.

elementos = input("Digite uma lista de elementos separados por espaço: ").split()
elementos_invertidos = elementos[::-1]
print("A lista invertida é:", elementos_invertidos)
