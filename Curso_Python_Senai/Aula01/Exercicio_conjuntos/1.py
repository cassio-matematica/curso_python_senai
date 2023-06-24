##Exercício 1: Verificar elementos duplicados
##Escreva um programa que recebe uma lista de números e verifica se existem elementos duplicados. Em seguida, exiba apenas os elementos únicos.

numeros = [1, 2, 3, 4, 4, 5, 6, 6, 7, 8, 9, 9]
conjunto = set(numeros)
elementos_unicos = list(conjunto)
print("Elementos únicos:", elementos_unicos)
