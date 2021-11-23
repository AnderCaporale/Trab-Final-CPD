def menu():
    """
    Função para imprimir o menu na tela
    () => int
    """
    print("\n\t=== MENU ===")
    print("1. Mostrar tempos de carregamento")
    print("2. Fazer uma pesquisa")
    print("3. Terminar o Programa\n")

    try:
        entrada = int(input("Escolha uma das opções: "))
        #Testa se a entrada é inválida
        while entrada < 1 or entrada > 3:
            print("Digite um numero entre 1 e 3!\n")
            entrada = int(input("Escolha uma das opções: "))
    except: 
        print("Digite um numero entre 1 e 3!")
        entrada = menu()

    return entrada

def mostrar_tempos(vetorTempos):
    #Players, rating, nomes, posicoes, tags, total
    print(f"\nTempo carregamento Players: {vetorTempos[0]}")
    print(f"Tempo carregamento Rating: {vetorTempos[1]}")
    print(f"Tempo carregamento Nomes: {vetorTempos[2]}")
    print(f"Tempo carregamento Posições: {vetorTempos[3]}")
    print(f"Tempo carregamento Tags: {vetorTempos[4]}")
    print(f"Tempo carregamento TOTAL: {vetorTempos[5]}\n")



'''
    if entrada == 1:
            prefix = str(input('Informe o prefixo de nome para consulta: '))
            pesquisaNomes(tabelaHashJogador,raizTrie,prefix)

    elif entrada == 2:
        idUser = int(input('Informe o id do Usuario: '))
        pesquisaUser(tabelaHashUsuario, tabelaHashJogador, idUser)

    elif entrada == 3:
        posicao = input('Informe a posição: ').lower()
        quantidade = int(input('Informe o número de jogadores: '))
        pesquisaPosicao(tabelaHashPosicoes, tabelaHashJogador, posicao, quantidade)

    elif entrada == 4:
        tags = input('Informe as tags: ').lower()
        buscarTags(tabelaHashTags, tabelaHashJogador, tags)
'''