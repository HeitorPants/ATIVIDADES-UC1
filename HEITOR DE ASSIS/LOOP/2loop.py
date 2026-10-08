soma = 0

for numero in range(1, 101):
    soma += numero

print("Resultado", soma)

for aluno in range(1, 6):
    nota = float(input("Digite a nota do aluno " + str(aluno) + ": "))

    if nota >= 7:
        print("Aprovado")
    elif nota >= 5:
        print("Recuperação")
    else:
        print("Reprovado")

numero = 1
for numero in range(1, 21):
    print(numero)
    numero += 1
numero % 2 
