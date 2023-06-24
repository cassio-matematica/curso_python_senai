lista_frutas = ["maçã", "banana", "melância", "abacate"]
lista_frutas.sort()
print(lista_frutas)

elemento_3 = lista_frutas[2]
print(elemento_3)

lista_frutas[0] = "jaca"
print(lista_frutas)

lista_frutas.append("carambola")
print(lista_frutas)

lista_frutas.insert(2,"nova_fruta")
print(lista_frutas)

for fruta in lista_frutas:
    if fruta == "maçã":
        print("Fruta: " , fruta)