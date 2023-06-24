##Exercício 2: Maior elemento
###Escreva um programa que recebe uma lista de números do usuário e retorna o maior elemento presente na lista.


"""numeros = input("Digite uma lista de números separados por espaço: ").split()
numeros = [int(num) for num in numeros]
maior = max(numeros)
print("O maior número é:", maior)"""

numero = input(" Digite uma lista de números com espaços").split()
numero = [int(num) for num in numero]


for valor in numero:
   
    if valor[0] > valor[1]:
        print(numero[0])
    else:
        print(numero[1])
    
    print(valor)
               

