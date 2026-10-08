#LETRA A
assentos = [
    [0, 1, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 1]
    ]

disponiveis = 0
ocupados = 0

for linha in assentos:
    for assento in linha:
        if assento == 0:
           disponiveis += 1
        else:
            assento == 1
            ocupados += 1
            
print("Assentos disponíveis: ",disponiveis)
print("Assentos ocupados: ",ocupados)

#LETRA B

linha = int(input("Escolha uma linha: "))
coluna = int(input("Escolha uma coluna: "))

if assentos[linha][coluna] == 0:
    print("O assento está disponível")
else:
    assentos[linha][coluna] == 1
    print("O assento está ocupado")