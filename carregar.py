from classes import *

def carregar_players(TabelaHash, planilha):
    for i in range(0, len(planilha.index)):
        insere_tabela_jogador(TabelaHash, planilha['sofifa_id'][i], planilha['name'][i], planilha['player_positions'][i], 131071)


def insere_tabela_jogador(tabela, id, nome, positions, tamanho):
    i = hash(id, tamanho)    #Encontra a posição hash

    if (tabela[i]):             #Se algum elemento já foi inserido, insere no fim
        tabela[i].append(Jogador(id, nome, positions))
    else:                       #Se não possui nenhum elemento, cria a lista encadeada e insere
        tabela[i] = []
        tabela[i].append(Jogador(id, nome, positions))


def carregar_rating(TabelaHashJogador, TabelaHashUsuario, planilha):
    for i in range(0, len(planilha.index)):
        rating = planilha['rating'][i]
        idJogador = planilha['sofifa_id'][i]
        insere_rating(TabelaHashJogador, idJogador, rating, 131071)
        insere_tabela_usuario(TabelaHashUsuario, planilha['user_id'][i], idJogador, rating, 524287)

def insere_rating(TabelaHash, id, rating, tamanho):
    i = hash(id, tamanho)
    soma_rating(TabelaHash[i], id, rating)

def soma_rating(lista, id, rating):
    if lista:
        for i in range(len(lista)):
            if (id == lista[i].id):   #Se encontra o id
                lista[i].soma += rating
                lista[i].qtd += 1

def insere_tabela_usuario(TabelaHashUsuario, idUsuario, idJogador, notaJogador, tamanho):
    i = hash(idUsuario, tamanho)        #Encontra a posição hash

    if (TabelaHashUsuario[i]):             #Se algum elemento já foi inserido, insere no fim
        append_usuario(TabelaHashUsuario[i], idUsuario, idJogador, notaJogador)
 
    else:                       #Se não possui nenhum elemento, cria a lista encadeada e insere
        TabelaHashUsuario[i] = []
        append_usuario(TabelaHashUsuario[i], idUsuario, idJogador, notaJogador)


def append_usuario(ListaHashUsuario, idUsuario, idJogador, notaJogador):
    novoUsuario = Usuario(idUsuario)
    adiciona_nota(novoUsuario.avaliacoes, idJogador, notaJogador)
    
    if ListaHashUsuario:
        for i in range(len(ListaHashUsuario)):
            if ListaHashUsuario[i].id == idUsuario: #Se o usuario já está na tabela hash
                adiciona_nota(ListaHashUsuario[i].avaliacoes, idJogador, notaJogador)
                return  #Apenas adiciona a nota e retorna

        ListaHashUsuario.append(novoUsuario)
        
    else:
        ListaHashUsuario.append(novoUsuario)


def adiciona_nota(AvaliacoesUsuario, jogadorId, notaJogador):
    novaAvaliacao = Avaliacao(jogadorId, notaJogador)

    if AvaliacoesUsuario:
        for i in range(len(AvaliacoesUsuario)):
            if notaJogador > AvaliacoesUsuario[i].notaJogador:
                AvaliacoesUsuario.insert(i, novaAvaliacao)
                return
        AvaliacoesUsuario.insert(len(AvaliacoesUsuario), novaAvaliacao)
        
    else:
        AvaliacoesUsuario.append(novaAvaliacao)



















