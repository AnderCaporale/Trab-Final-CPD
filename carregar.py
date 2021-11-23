import csv
from classes import *
from classeTrie import *
from time import perf_counter

def carregamento(tabelaHashJogador, tabelaHashUsuario, tabelaHashPosicoes, tabelaHashTags, raizTrie, vetorTempos):
    inicioTimer = perf_counter()
    carregar_players(tabelaHashJogador)     #Carrega os Jogadores na tabela hash
    fimTimer = perf_counter()
    vetorTempos[0] = fimTimer - inicioTimer     #Salva o tempo gasto

    inicioTimer = perf_counter()
    carregar_rating(tabelaHashJogador, tabelaHashUsuario)   #Carrega os Usuarios na tabela hash e as avaliações dos jogadores
    fimTimer = perf_counter()
    vetorTempos[1] = fimTimer - inicioTimer

    inicioTimer = perf_counter()
    carregar_nomes(raizTrie)  # Carrega os Usuarios na tabela hash e as avaliações dos jogadores
    fimTimer = perf_counter()
    vetorTempos[2] = fimTimer - inicioTimer

    inicioTimer = perf_counter()
    carregar_posicoes(tabelaHashPosicoes)    #Carrega os ids nas devidas posições
    fimTimer = perf_counter()
    vetorTempos[3] = fimTimer - inicioTimer

    inicioTimer = perf_counter()
    carregar_tags(tabelaHashTags)    #Carrega as tags nas devidas posições
    fimTimer = perf_counter()
    vetorTempos[4] = fimTimer - inicioTimer


def carregar_players(TabelaHashJogador):
    file = open('players.csv', mode='r')
    planilha = csv.reader(file)
    next(planilha)
    for linha in planilha: #Le a planilha de jogadores linha a linha
        idJogador = int(linha[0])
        nomeJogador = linha[1]
        posicoes = linha[2].split(', ')
        insere_tabela_jogador(TabelaHashJogador, idJogador, nomeJogador, posicoes)
    file.close()


def insere_tabela_jogador(tabela, id, nome, positions):
    i = hash(id, tamanho_tabelaHashJogador)       #Encontra a posição hash

    if tabela[i]:             #Se algum elemento já foi inserido, insere no fim
        tabela[i].append(Jogador(id, nome, positions))
    else:                       #Se não possui nenhum elemento, cria a lista e insere
        tabela[i] = []
        tabela[i].append(Jogador(id, nome, positions))


def carregar_rating(TabelaHashJogador, TabelaHashUsuario):
    file = open('rating.csv', mode='r')
    planilha = csv.reader(file)
    next(planilha)
    for linha in planilha:  # Le a planilha de jogadores linha a linha
        rating = float(linha[2])    #Le a nota dada
        idJogador = int(linha[1])   #Le o ID do Jogador
        user = int(linha[0])        #Le o ID do user
        insere_rating(TabelaHashJogador, idJogador, rating)
        insere_tabela_usuario(TabelaHashUsuario, user, idJogador, rating)
    file.close()

def insere_rating(TabelaHash, id, rating):
    i = hash(id, tamanho_tabelaHashJogador) #Encontra a posição hash
    soma_rating(TabelaHash[i], id, rating)


def soma_rating(lista, id, rating):
    if lista:                               #Se a lista de jogadores não é vazia
        for i in range(len(lista)):
            if (id == lista[i].id):         #Se encontra o id
                lista[i].soma += rating     #Faz a soma
                lista[i].qtd += 1           #Aumenta a quantidade de avaliações
                return                      #Retorna depois que acha


def insere_tabela_usuario(TabelaHashUsuario, idUsuario, idJogador, notaJogador):
    i = hash(idUsuario, tamanho_tabelaHashUsuario)  #Encontra a posição hash

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


def carregar_nomes(raiz:Trie):
    """colocar os nomes em um árvore trie"""
    file = open('players_clean2.csv', mode='r')
    planilha = csv.reader(file)
    next(planilha)
    for linha in planilha:  # Le a planilha de jogadores linha a linha
        nome = linha[1]
        id_jogador = int(linha[0])
        raiz.insere_nodo(nome,id_jogador)
    file.close()

def carregar_posicoes(TabelaHashPosicoes):
    file = open('players_clean2.csv', mode='r')
    planilha = csv.reader(file)
    next(planilha)
    for linha in planilha:  # Le a planilha de jogadores linha a linha
        idJogador = int(linha[0])
        posicoes = linha[2].split(',')
        insere_tabela_posicoes(TabelaHashPosicoes, posicoes, idJogador)
    file.close()

def insere_tabela_posicoes(TabelaHashPosicoes, posicoes, idJogador):
    for i in range(len(posicoes)):
        novaPosicao = Posicao(posicoes[i].lower().strip())      #Cria uma nova posição
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


def carregar_tags(TabelaHashTags):
    file = open('tags.csv', mode='r')
    planilha = csv.reader(file)
    next(planilha)
    for linha in planilha:  # Le a planilha de tags linha a linha
        idJogador = int(linha[1])
        tag = linha[2]
        insere_tabela_tags(TabelaHashTags, tag, idJogador)
    file.close()

def insere_tabela_tags(TabelaHashTags, tag, idJogador):
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
