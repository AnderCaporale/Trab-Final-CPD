from classes import *
from classeTrie import *
from time import perf_counter

def carregamento(tabelaHashJogador, tabelaHashUsuario, tabelaHashPosicoes, tabelaHashTags, planilhaPlayer, planilhaRating, planilhaTags, raizTrie):
    inicioTimer = perf_counter()
    carregar_players(tabelaHashJogador, planilhaPlayer,tamanho_tabelaHashJogador)     #Carrega os Jogadores na tabela hash
    fimTimer = perf_counter()
    print(f"Tempo carrega players: {fimTimer - inicioTimer} segundos")

    inicioTimer = perf_counter()
    carregar_rating(tabelaHashJogador, tabelaHashUsuario, planilhaRating,tamanho_tabelaHashJogador,tamanho_tabelaHashUsuario)   #Carrega os Usuarios na tabela hash e as avaliações dos jogadores
    fimTimer = perf_counter()
    print(f"Tempo carrega rating: {fimTimer - inicioTimer} segundos")
    
    inicioTimer = perf_counter()
    carregar_nomes(raizTrie,planilhaPlayer)  # Carrega os Usuarios na tabela hash e as avaliações dos jogadores
    fimTimer = perf_counter()
    print(f"Tempo carrega nomes: {fimTimer - inicioTimer} segundos")

    inicioTimer = perf_counter()
    carregar_posicoes(tabelaHashPosicoes, planilhaPlayer, tamanho_tabelaHashPosicoes)    #Carrega os ids nas devidas posições
    fimTimer = perf_counter()
    print(f"Tempo carrega posicoes: {fimTimer - inicioTimer} segundos")

    inicioTimer = perf_counter()
    carregar_tags(tabelaHashTags, planilhaTags, tamanho_tabelaHashTags)    #Carrega as tags nas devidas posições
    fimTimer = perf_counter()
    print(f"Tempo carrega tags: {fimTimer - inicioTimer} segundos")


def carregar_players(TabelaHashJogador, planilha, tamanho_tabelaHashJogador):
    for i in range(0, len(planilha.index)): #Le a planilha de jogadores linha a linha
        nomeJogador = planilha['name'][i]
        idJogador = planilha['sofifa_id'][i]
        posicoes = planilha['player_positions'][i].split(', ')
        insere_tabela_jogador(TabelaHashJogador, idJogador, nomeJogador, posicoes, tamanho_tabelaHashJogador)


def insere_tabela_jogador(tabela, id, nome, positions, tamanho):
    i = hash(id, tamanho)       #Encontra a posição hash

    if tabela[i]:             #Se algum elemento já foi inserido, insere no fim
        tabela[i].append(Jogador(id, nome, positions))
    else:                       #Se não possui nenhum elemento, cria a lista e insere
        tabela[i] = []
        tabela[i].append(Jogador(id, nome, positions))


def carregar_rating(TabelaHashJogador, TabelaHashUsuario, planilha, tamanho_tabelaHashJogador, tamanho_tabelaHashUsuario):
    for i in range(0, len(planilha.index)):     #Le a planilha de rating linha a linha
        rating = planilha['rating'][i]          #Le a nota dada
        idJogador = planilha['sofifa_id'][i]    #Le o ID do Jogador
        inicioTimer = perf_counter()
        insere_rating(TabelaHashJogador, idJogador, rating, tamanho_tabelaHashJogador)
        insere_tabela_usuario(TabelaHashUsuario, planilha['user_id'][i], idJogador, rating, tamanho_tabelaHashUsuario)


def insere_rating(TabelaHash, id, rating, tamanho):
    i = hash(id, tamanho)                       #Encontra a posição hash
    soma_rating(TabelaHash[i], id, rating)


def soma_rating(lista, id, rating):
    if lista:                               #Se a lista de jogadores não é vazia
        for i in range(len(lista)):
            if (id == lista[i].id):         #Se encontra o id
                lista[i].soma += rating     #Faz a soma
                lista[i].qtd += 1           #Aumenta a quantidade de avaliações
                return                      #Retorna depois que acha


def insere_tabela_usuario(TabelaHashUsuario, idUsuario, idJogador, notaJogador, tamanho):
    i = hash(idUsuario, tamanho)            #Encontra a posição hash

    if (TabelaHashUsuario[i]):              #Se algum elemento já foi inserido, insere no fim
        append_usuario(TabelaHashUsuario[i], idUsuario, idJogador, notaJogador)

    else:                                   #Se não possui nenhum elemento, cria a lista encadeada e insere
        TabelaHashUsuario[i] = []
        append_usuario(TabelaHashUsuario[i], idUsuario, idJogador, notaJogador)


def append_usuario(ListaHashUsuario, idUsuario, idJogador, notaJogador):
    novoUsuario = Usuario(idUsuario)        #Cria novo usuario
    adiciona_nota(novoUsuario.avaliacoes, idJogador, notaJogador)   #Adiciona a avaliação nesse usuario

    if ListaHashUsuario:                    #Se algum elemento já foi inserido
        for i in range(len(ListaHashUsuario)):
            if ListaHashUsuario[i].id == idUsuario: #Se o usuario já está na tabela hash
                adiciona_nota(ListaHashUsuario[i].avaliacoes, idJogador, notaJogador)
                return  #Apenas adiciona a nota e retorna

        ListaHashUsuario.append(novoUsuario)        #Se o usuario nao está na lista, adiciona no fim

    else:                                   #Se não possui nenhum elemento, insere no fim
        ListaHashUsuario.append(novoUsuario)


def adiciona_nota(AvaliacoesUsuario, jogadorId, notaJogador):
    novaAvaliacao = Avaliacao(jogadorId, notaJogador)   #Cria nova Avaliação
    AvaliacoesUsuario.append(novaAvaliacao)


def carregar_nomes(raiz:Trie,planilha):
    """colocar os nomes em um árvore trie"""
    for i in range(0, len(planilha.index)):#Le a planilha de rating linha a linha
        nome = planilha['name'][i]
        id_jogador = planilha['sofifa_id'][i]
        raiz.insere_nodo(nome,id_jogador)

def carregar_posicoes(TabelaHashPosicoes, planilha, tamanho_tabelaHashPosicoes):
    for i in range(0, len(planilha.index)): #Le a planilha de jogadores linha a linha
        idJogador = planilha['sofifa_id'][i]
        posicoes = planilha['player_positions'][i].split(', ')
        insere_tabela_posicoes(TabelaHashPosicoes, posicoes, idJogador, tamanho_tabelaHashPosicoes)


def insere_tabela_posicoes(TabelaHashPosicoes, posicoes, idJogador, tamanho_tabelaHashPosicoes):
    for i in range(len(posicoes)):
        novaPosicao = Posicao(posicoes[i].lower())      #Cria uma nova posição
        novaPosicao.ids.append(idJogador)

        h = hash_palavras(posicoes[i].lower(), tamanho_tabelaHashPosicoes)
        if(TabelaHashPosicoes[h]):  #Se alguma posição ja foi inserida na tabela hash
            for j in range(len(TabelaHashPosicoes[h])):     #Procura a posição na tabela hash
                if TabelaHashPosicoes[h][j].nome == posicoes[i].lower():        #Achou posição correta
                    if idJogador not in TabelaHashPosicoes[h][j].ids:   #Se ID Não está na lista de ids
                        TabelaHashPosicoes[h][j].ids.append(idJogador)  #Adiciona o ID na lista
                    
        else:   #Se nenhuma posição foi inserida
            TabelaHashPosicoes[h] = []                  #Cria a lista e insere a nova posição
            TabelaHashPosicoes[h].append(novaPosicao)


def carregar_tags(TabelaHashTags, planilhaTags, tamanho_tabelaHashTags):
    for i in range(0, len(planilhaTags.index)): #Le a planilha de jogadores linha a linha
        idJogador = planilhaTags['sofifa_id'][i]
        tag = planilhaTags['tag'][i]
        insere_tabela_tags(TabelaHashTags, tag, idJogador, tamanho_tabelaHashTags)


def insere_tabela_tags(TabelaHashTags, tag, idJogador, tamanho_tabelaHashTags):
    if isinstance(tag, str):
        novaTag = Tag(tag.lower())              #Cria uma nova tag
        novaTag.ids.append(idJogador)
        
        h = hash_palavras(tag.lower(), tamanho_tabelaHashTags)

        if(TabelaHashTags[h]):  #Se alguma posição ja foi inserida na tabela hash
            for j in range(len(TabelaHashTags[h])):     #Procura a posição na tabela hash
                if TabelaHashTags[h][j].nome == tag.lower():        #Achou posição correta
                    if idJogador not in TabelaHashTags[h][j].ids:   #Se ID Não está na lista de ids
                        TabelaHashTags[h][j].ids.append(idJogador)  #Adiciona o ID na lista
                    
        else:   #Se nenhuma posição foi inserida
            TabelaHashTags[h] = []                  #Cria a lista e insere a nova posição
            TabelaHashTags[h].append(novaTag)
