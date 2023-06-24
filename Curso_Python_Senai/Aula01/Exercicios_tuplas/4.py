##Exercício 4: Verificação de existência
##Escreva um programa que declare uma tupla e verifique se um elemento específico está presente nela.

tupla = (10, 20, 30, 40, 50)
elemento = 30
if elemento in tupla:
    print("O elemento", elemento, "está presente na tupla.")
else:
    print("O elemento", elemento, "não está presente na tupla.")
