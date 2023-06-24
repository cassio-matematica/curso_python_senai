##Exercício 4: Calcular o fatorial de um número usando um loop "for".

n = int(input("Digite um número: "))
fatorial = 1
for i in range(1, n+1):
    fatorial *= i
print("O fatorial de", n, "é", fatorial)
