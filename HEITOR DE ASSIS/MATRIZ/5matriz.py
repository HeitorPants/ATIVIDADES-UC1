matriz = [
    [7, 8, 9],
    [5, 6, 7],
    [8, 9, 10]
    ]

soma = 0

for linha in matriz:
    for numero in linha:
        soma = soma + numero

print("Soma: ", soma)

media = soma / 2

print("Media dos valores somados: ",media)

maior = matriz[0][0]

for linha in matriz:
    for numero in linha:
        if numero > maior:
            maior = numero

print("Maior numero: ", maior)

menor = matriz[0][0]

for linha in matriz:
    for numero in linha:
        if numero < menor:
            menor = numero

print("Menor numero: ", menor)