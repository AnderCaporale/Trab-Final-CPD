import pandas as pd
from time import perf_counter
from menu import *
from carregar import *
from classes import *
from funcao2 import *
from classeTrie import *
from funcao1 import *
from funcao3 import *
from funcao4 import *


def main():
    planilhaPlayer = pd.read_csv("players_clean2.csv", delimiter = ",") #Le a planilha
    planilhaRating = pd.read_csv("rating.csv", delimiter = ",")     #Le a planilha
    planilhaTags = pd.read_csv("tags.csv", delimiter = ",")             #Le a planilha
    tabelaHashJogador = [None] * 131071                     #Cria tabela hash para os Jogadores
    tabelaHashUsuario = [None] * 524287                     #Cria tabela hash para os Usuarios
    tabelaHashPosicoes = [None] * 7001                      #Cria tabela hash para as Posições
    tabelaHashTags = [None] * 7013                          #Cria tabela hash para as Tags
    raizTrie = Trie()

    inicioTimerTotal = perf_counter()
    carregamento(tabelaHashJogador, tabelaHashUsuario, tabelaHashPosicoes, tabelaHashTags, planilhaPlayer, planilhaRating, planilhaTags, raizTrie)
    fimTimerTotal = perf_counter()
    print(f"TEMPO TOTAL: {fimTimerTotal - inicioTimerTotal} segundos")
    
    entrada = 0
    #Fica no loop até a entrada ser a opção 5
    while entrada != 5:
        entrada = menu()

        if entrada == 1:
            prefix = str(input('Informe o prefixo de nome para consulta: '))
            pesquisaNomes(tabelaHashJogador,raizTrie,planilhaPlayer,prefix)

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

        else:
            print("Programa Encerrado!")

main()
