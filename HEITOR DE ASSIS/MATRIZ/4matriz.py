matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
print("Elemento da linha 0, coluna 1:", matriz[0][1])
print("Elemento da linha 1, coluna 2:", matriz[1][2])
print("Elemento da linha 2, coluna 0:", matriz[2][0])

matriz = [
    [5, 8, 3],
    [2, 7, 9],
    [4, 6, 1]
    ]

for linha in matriz:
    print(linha)

for linha in matriz:
    for numero in linha:
        if numero % 2 == 0:
            print("Apenas numeros pares: ",numero)

for linha in matriz:
    for numero in linha:
        if numero > 5:
            print("Apenas numeros maiores que 5: ",numero)