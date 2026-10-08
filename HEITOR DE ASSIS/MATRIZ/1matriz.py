matriz = [
    [10, 20],
    [30, 40]
]

matriz[0][1] = 99
print(matriz)

matriz = [
    [10, 20, 30],
    [40, 50, 60]
]

for linha in matriz:
    for numero in linha:
        print(numero)