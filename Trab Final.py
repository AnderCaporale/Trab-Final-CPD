import pandas as pd
from time import perf_counter
from menu import *
from carregar import *
from classes import *
from funcao2 import *
from classeTrie import *
from funcao1 import *
from funcao3 import *

def main():
    planilhaPlayer = pd.read_csv("players.csv", delimiter = ",") #Le a planilha
    planilhaRating = pd.read_csv("minirating.csv", delimiter = ",") #Le a planilha
    TabelaHashJogador = [None] * 131071                     #Cria tabela hash para os Jogadores
    TabelaHashUsuario = [None] * 524287                     #Cria tabela hash para os Usuarios
    TabelaHashPosicoes = [None] * 7001                      #Cria tabela hash para as Posições
    raizTrie = Trie()

    inicioTimer = perf_counter()
    carregar_players(TabelaHashJogador, TabelaHashPosicoes, planilhaPlayer)     #Carrega os Jogadores na tabela hash
    fimTimer = perf_counter()
    print(f"Tempo carrega players: {fimTimer - inicioTimer} segundos")

    inicioTimer = perf_counter()
    carregar_rating(TabelaHashJogador, TabelaHashUsuario, planilhaRating)   #Carrega os Usuarios na tabela hash e as avaliações dos jogadores
    fimTimer = perf_counter()
    print(f"Tempo carrega rating: {fimTimer - inicioTimer} segundos")

    inicioTimer = perf_counter()
    carregar_nomes(raizTrie,planilhaPlayer)  # Carrega os Usuarios na tabela hash e as avaliações dos jogadores
    fimTimer = perf_counter()
    print(f"Tempo carrega nomes: {fimTimer - inicioTimer} segundos")


    inicioTimer = perf_counter()
    carregar_posicoes(TabelaHashJogador, TabelaHashPosicoes, planilhaPlayer)    #Carrega os ids nas devidas posições
    fimTimer = perf_counter()
    print(f"Tempo carrega posicoes: {fimTimer - inicioTimer} segundos")
    
    entrada = 0
    #Fica no loop até a entrada ser a opção 6
    while entrada != 5:
        entrada = menu()

        if entrada == 1:
            prefix = str(input('Informe o prefixo de nome para consulta: '))
            pesquisaNomes(TabelaHashJogador,raizTrie,planilhaPlayer,prefix)
        elif entrada == 2:
            idUser = int(input('Informe o id do Usuario: '))
            i = hash(idUser, 524287)
            print()
            pesquisaUser(TabelaHashUsuario[i], TabelaHashJogador, idUser, planilhaRating)
            
        elif entrada == 3:
            posicao = input('Informe a posição: ')
            quantidade = int(input('Informe o número de jogadores: '))
            pesquisaPosicao(TabelaHashPosicoes, TabelaHashJogador, posicao, quantidade)

        elif entrada == 4:
            pass
            #funcao4()
        else:
            print("Programa Encerrado!")

main()



