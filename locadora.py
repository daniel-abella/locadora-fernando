filmes = []

while True:
    print("\n1) Listar \n2) Adicionar \n3) Pesquisar \n4) Remover \n5) Quantidade de Filmes \n6) Substituir \n7) Sair")
    opcao = int(input("Digite a sua opção: "))

    if opcao == 1:
        if len(filmes) > 0:
            print("Lista de Filmes")
            for item in filmes:
                print("-", item)

        else:
            print("Nenhum filme foi encontrado")

    elif opcao == 2:
        novo_filme = input("Informe o nome do novo filme: ")
        filmes.append(novo_filme)
        print("Filme adicionado com sucesso!")

    elif opcao == 3:
        codigo = int(input("Informe a codigo do filme: "))

        if codigo >= 1 and codigo <= len(filmes):
            filme_pesquisado = filmes[codigo - 1]
            print("O filme pesquisado foi", filme_pesquisado)

        else:
            print("O código informado é inválido.")

    elif opcao == 4:
        codigo = int(input("Informe a codigo do filme a ser removido: "))

        if codigo >= 1 and codigo <= len(filmes):
            filmes.pop(codigo - 1)
            print("Filme removido com sucesso!")

        else:
            print("O código informado é inválido.")

    elif opcao == 5:
        print("Atualmente tem(os)", len(filmes), "filme(s)")

    elif opcao == 6:
        codigo = int(input("Informe a codigo do filme a ser substituído: "))

        if codigo >= 1 and codigo <= len(filmes):
            nome_novo_filme = input("Informe o nome do novo filme: ")
            filmes[codigo - 1] = nome_novo_filme
            print("Filme substituído com sucesso!")

        else:
            print("O código informado é inválido.")

    elif opcao == 7:
        break

    else:
        print("Opção Inválida.")

print("Obrigado")