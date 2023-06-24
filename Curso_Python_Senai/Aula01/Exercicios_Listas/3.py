##Exercício 3: Contagem de elementos pares
#Escreva um programa que recebe uma lista de números do usuário e retorna a quantidade de elementos pares presentes na lista.

numeros = input("Digite uma lista de números separados por espaço: ").split()
numeros = [int(num) for num in numeros]
contagem = 0
for num in numeros:
    if num % 2 == 0:
        contagem += 1
print("A quantidade de números pares é:", contagem)
