lista_de_compras = []
while True:
    try:
        print("Selecione uma opção")
        opcao = input('[i]nserir [a]pagar [l]istar: ')
        if opcao == 'i':
            novo_item = input("Valor: ")
            lista_de_compras.append(novo_item)
        elif opcao == 'a':
            try:
                tirar_item = input("Digite qual íncdice você deseja apagar: ")
                lista_de_compras.pop(int(tirar_item))
            except ValueError:
                print("Digite um número inteiro")
            except IndexError:
                print('Índice não encontrado')
        elif opcao == 'l':
            lista_enumerada = list(enumerate(lista_de_compras))
            for indice, valor in lista_enumerada:
                print(lista_de_compras)
    except:
        print('Digite uma opção válida')
