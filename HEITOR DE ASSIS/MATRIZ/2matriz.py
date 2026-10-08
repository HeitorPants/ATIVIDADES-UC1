matriz = [
    [10, 20, 30],
    [40, 50, 60]
]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print("Linha:", i)
        print("Coluna:", j)
        print("Valor:", matriz[i][j])