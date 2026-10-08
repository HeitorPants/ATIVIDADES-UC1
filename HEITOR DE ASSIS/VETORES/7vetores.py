alunos = []

for i in range(5):
    aluno = input("Digite seu nome: ")
    alunos.append(aluno)

    i = 0

while i < len(alunos):
    print(alunos[i])
    i += 1