opcao = -1

while opcao != 0:
    print("1 - Consultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("0 - Sair")

    opcao = int(input("Escolha: "))

    if opcao == 1:
        print("Consultando saldo...")
    elif opcao == 2:
        print("Realizando deposito...")
    elif opcao == 3:
        print("Realizanfo saque...")
    elif opcao == 0:
        print("Encerrando...")
    else:
        print("Opçãp invalida")