##Exercício 4: Verificar diferença
##Escreva um programa que declare dois conjuntos de números (conjunto1 e conjunto2) e exiba os números que estão presentes apenas em conjunto1, mas não em conjunto2.

conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}
diferenca = conjunto1.difference(conjunto2)
print("Números exclusivos em conjunto1:", diferenca)
