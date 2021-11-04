from classes import *

def buscaListaAvaliacoes(ListaHashUsuario, index):
    lista = ListaHashUsuario.avaliacoes
    return lista[index].idJogador, lista[index].notaJogador 

def buscaJogadores(TabelaHashJogador, i, idJogador):
    if TabelaHashJogador[i]:
        for j in range(len(TabelaHashJogador[i])):
            if (idJogador == TabelaHashJogador[i][j].id):   #Se encontra o id
                return TabelaHashJogador[i][j].nome, TabelaHashJogador[i][j].soma, TabelaHashJogador[i][j].qtd

def pesquisaUser(ListaHashUsuario, TabelaHashJogador, idUser):
    j = 0
    for i in range(len(ListaHashUsuario)):
        if ListaHashUsuario[i] == idUser:
            break
    print ("{:<15} {:<40} {:<15} {:<15} {:<15}".format('Fifa ID','Name','Global Rating', 'Count', 'Rating'))
    while j < 20 and j < len(ListaHashUsuario[i].avaliacoes):
        idJogador, notaJogador = buscaListaAvaliacoes(ListaHashUsuario[i], j)
        h = hash(idJogador, 131071)
        nomeJogador, somaJogador, qtdJogador = buscaJogadores(TabelaHashJogador, h, idJogador)
        global_rating = somaJogador / qtdJogador        
        print("{:<15} {:<40} {:<15} {:<15} {:<15}".format(idJogador, nomeJogador, global_rating, somaJogador, notaJogador))

        j+=1