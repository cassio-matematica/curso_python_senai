###Calculadora
def apresentacao():
    print("###########################################\n")
    print("Bem vindo a calculadora do curso de Python\n")
    print("###########################################\n")

apresentacao()

numero1= int(input("Digite o primeiro número:\n"))
numero2 = int(input("Digite o segundo número:\n"))

print("########################")
print("Operacões diponiveis:\n")
print("Opçaõ 1: ***Soma***\n")
print("Opção 2:***Subtração***\n")
print("Opção 3:***Divisão***\n")
print("Opção 4: ***Multiplição***\n")

def soma(a,b):
    return a + b

def subtracao(a,b):
    return a - b

def multiplicacao(a, b):
    return a*b

def divisao (a,b):
    return a/b

operacao =input("Escolha uma operacao:")
num = int(operacao)
if num == 1:
    soma(numero1, numero2)
    print("o resultado da operação é:")
    resultado =soma(numero1,numero2)
    print(resultado)

elif num == 2:
    subtracao(numero1, numero2)
    print("o resultado da operação é:")
    resultado =subtracao(numero1,numero2)
    print(resultado)

elif num == 3:
    divisao(numero1, numero2)
    print("o resultado da operação é:")
    resultado =divisao(numero1,numero2)
    print(resultado)

elif num == 4:
    multiplicacao(numero1,numero2)
    print("o resultado da operação é:")
    resultado =multiplicacao(numero1,numero2)
    print(resultado)
    
else:
    print("Operação invalida.")






    

