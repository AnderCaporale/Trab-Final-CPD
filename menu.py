def menu():
    """
    Função para imprimir o menu na tela
    () => int
    """
    print("\n\t=== MENU ===")
    print("1. Pesquisas sobre os nomes de jogadores")
    print("2. Pesquisas sobre jogadores revisados por usuários")
    print("3. Pesquisas sobre os melhores jogadores de uma determinada posição")
    print("4. Pesquisas sobre ‘tags’ de jogadores")
    print("5. Terminar o Programa\n")

    #Se é digitado algo além de 1 número, dá erro
    try:
        entrada = int(input("Escolha uma das opções: "))
        #Testa se a entrada é inválida
        while entrada < 1 or entrada > 5:
            print("Digite um numero entre 1 e 5!\n")
            entrada = int(input("Escolha uma das opções: "))
    except: 
        print("Digite um numero entre 1 e 5!")
        entrada = menu()

    return entrada