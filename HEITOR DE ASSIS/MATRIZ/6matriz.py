matriz = []

for i in range(2):
    linha = []

    for j in range(3):
        numero = int(input("Digite um número: "))
        linha.append(numero)

    matriz.append(linha)

for linha in matriz:
    print(linha)