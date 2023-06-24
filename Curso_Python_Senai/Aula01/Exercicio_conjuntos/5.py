##Exercício 5: Verificar subconjunto
##Escreva um programa que declare dois conjuntos de letras (conjunto1 e conjunto2) e verifique se conjunto1 é um subconjunto de conjunto2.

conjunto1 = {'a', 'b', 'c'}
conjunto2 = {'a', 'b', 'c', 'd', 'e'}
if conjunto1.issubset(conjunto2):
    print("conjunto1 é um subconjunto de conjunto2")
else:
    print("conjunto1 não é um subconjunto de conjunto2")
