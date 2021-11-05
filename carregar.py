from classes import *

def carregar_players(TabelaHash, planilha):
    for i in range(0, len(planilha.index)): #Le a planilha de jogadores linha a linha
        insere_tabela_jogador(TabelaHash, planilha['sofifa_id'][i], planilha['name'][i], planilha['player_positions'][i], 131071)


def insere_tabela_jogador(tabela, id, nome, positions, tamanho):
    i = hash(id, tamanho)       #Encontra a posição hash

    if (tabela[i]):             #Se algum elemento já foi inserido, insere no fim
        tabela[i].append(Jogador(id, nome, positions))
    else:                       #Se não possui nenhum elemento, cria a lista e insere
        tabela[i] = []
        tabela[i].append(Jogador(id, nome, positions))


def carregar_rating(TabelaHashJogador, TabelaHashUsuario, planilha):
    for i in range(0, len(planilha.index)):     #Le a planilha de rating linha a linha
        rating = planilha['rating'][i]          #Le a nota dada
        idJogador = planilha['sofifa_id'][i]    #Le o ID do Jogador
        insere_rating(TabelaHashJogador, idJogador, rating, 131071)
        insere_tabela_usuario(TabelaHashUsuario, planilha['user_id'][i], idJogador, rating, 524287)


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



#Busca Linear
def adiciona_nota(AvaliacoesUsuario, jogadorId, notaJogador):
    novaAvaliacao = Avaliacao(jogadorId, notaJogador)   #Cria nova Avaliação

    if AvaliacoesUsuario:       #Se já possui alguma avaliação na lista
        for i in range(len(AvaliacoesUsuario)):
            if notaJogador > AvaliacoesUsuario[i].notaJogador:
                AvaliacoesUsuario.insert(i, novaAvaliacao)  #Insere na posição correta
                return
            if i > 20:          #Se não está entre as 20 maiores, não faz nada
                return

        AvaliacoesUsuario.insert(len(AvaliacoesUsuario), novaAvaliacao)
        
    else:
        AvaliacoesUsuario.append(novaAvaliacao)

'''
#Busca binaria
#Recebe uma lista, um id e uma nota
def adiciona_nota(AvaliacoesUsuario, jogadorId, notaJogador):
    novaAvaliacao = Avaliacao(jogadorId, notaJogador)       #Cria nova Avaliação
    limite = 20     #Salva só 20 maiores avaliações

    if AvaliacoesUsuario:               #Se já possui alguma avaliação na lista
        if len(AvaliacoesUsuario) >= limite:        #Verifica se ja tem 20 avaliações
            #Se a nota é menor ou igual que as 20 maiores, não faz nada
            if notaJogador <= AvaliacoesUsuario[limite-1].notaJogador:     
                return

        #Se faz parte das 20 maiores, insere na posição correta
        AvaliacoesUsuario.insert(busca_binaria(AvaliacoesUsuario, notaJogador), novaAvaliacao)
            
    else:           #Se não possui nenhum elemento, insere no fim
        AvaliacoesUsuario.append(novaAvaliacao)


#Faz a busca binaria e retorna a posição que deve ser inserido
def busca_binaria(lista, item):
    inicio = 0
    ultimo = len(lista)-1
    found = False
    posicao = 0

    while inicio <= ultimo and not found:
        meio = (inicio + ultimo)//2
        
        if lista[meio].notaJogador == item:
            found = True
            posicao = meio
        else:
            if item > lista[meio].notaJogador:
                ultimo = meio-1
                posicao = ultimo
            else:
                inicio = meio+1
                posicao = inicio

    if posicao < 0:
        return 0
    return posicao
'''













