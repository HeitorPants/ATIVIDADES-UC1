matriz = []

for i in range(3):
    linha = []

    for j in range(3):
        numero = int(input("Digite um número: "))
        linha.append(numero)

    matriz.append(linha)

#print(matriz)

for linha in matriz:
    print(linha)

soma = 0
quantidade = 0

for linha in matriz:
    for numero in linha:
        soma = soma + numero

print("Soma: ", soma)

for linha in matriz:
    for numero in linha:
        if numero % 2 == 0:
            quantidade += 1

            print(numero)

print("Quantidade de pares: ", quantidade)

maior = matriz[0][0]

for linha in matriz:
    for numero in linha:
        if numero > maior:
            maior = numero

print("Maior: ", maior)

somalinha = 0

for numero in matriz[0]:
    somalinha += numero

print ("Soma da primeira linha:", somalinha)

somacoluna = 0

for i in range(len(matriz)):
    somacoluna += matriz[i][0]

print ("Soma da primeira coluna:", somacoluna)