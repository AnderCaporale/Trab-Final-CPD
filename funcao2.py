from classes import *

#Recebe uma lista, uma tabela hash e um id de usuario
def pesquisaUser(ListaHashUsuario, TabelaHashJogador, idUser):
    j = 0
    i = 0
    for i in range(len(ListaHashUsuario)):  #Procura o usuario caso haja colisoes e salva o indice no i
        if ListaHashUsuario[i] == idUser:
            break
    
    #Imprime cabeçalho da tabela
    print ("{:<15} {:<40} {:<15} {:<15} {:<15}".format('Fifa ID','Name','Global Rating', 'Count', 'Rating'))

    while j < 20 and j < len(ListaHashUsuario[i].avaliacoes):   #Imprime os 20 primeiros ou menos
        idJogador, notaJogador = buscaListaAvaliacoes(ListaHashUsuario[i], j)   #Pega o ID e a nota da avaliação
        h = hash(idJogador, 131071) #Calcula a posição hash
        nomeJogador, somaJogador, qtdJogador = buscaJogadores(TabelaHashJogador, h, idJogador)
        global_rating = somaJogador / qtdJogador    #Faz a média global das avaliações

        #Imprime em formato de tabela
        print("{:<15} {:<40} {:<15.6} {:<15} {:<15}".format(idJogador, nomeJogador, global_rating, qtdJogador, notaJogador))

        j+=1

#Pega a lista de avaliações e retorna o ID e a nota do jogador conforme o indice passado
def buscaListaAvaliacoes(ListaHashUsuario, index):
    lista = ListaHashUsuario.avaliacoes             
    return lista[index].idJogador, lista[index].notaJogador 

#Procura o id do jogador na tabela hash e verifica colisao, depois retorna o nome, a soma e a qtd de avaliações
def buscaJogadores(TabelaHashJogador, h, idJogador):
    if TabelaHashJogador[h]:
        for j in range(len(TabelaHashJogador[h])):      #Trata as colisoes
            if (idJogador == TabelaHashJogador[h][j].id):   #Se encontra o id
                return TabelaHashJogador[h][j].nome, TabelaHashJogador[h][j].soma, TabelaHashJogador[h][j].qtd

