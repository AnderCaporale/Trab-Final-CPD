import csv
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
    
    tabelaHashJogador = [None] * tamanho_tabelaHashJogador                     #Cria tabela hash para os Jogadores
    tabelaHashUsuario = [None] * tamanho_tabelaHashUsuario                     #Cria tabela hash para os Usuarios
    tabelaHashPosicoes = [None] * tamanho_tabelaHashPosicoes                      #Cria tabela hash para as Posições
    tabelaHashTags = [None] * tamanho_tabelaHashTags                          #Cria tabela hash para as Tags
    raizTrie = Trie()
    vetorTempos = [0,0,0,0,0,0]     #Players, rating, nomes, posicoes, tags, total

    inicioTempoTotal = perf_counter()
    carregamento(tabelaHashJogador, tabelaHashUsuario, tabelaHashPosicoes, tabelaHashTags, raizTrie, vetorTempos)
    fimTempoTotal = perf_counter()
    vetorTempos[5] = fimTempoTotal - inicioTempoTotal

    entrada = 0
    #Fica no loop até a entrada ser a opção 5
    while entrada != 3:
        entrada = menu()

        if entrada == 1:
            mostrar_tempos(vetorTempos)

        elif entrada == 2:
            print("Utilize as consultas player, user, top** ou tags: ")
            pesquisa = input().lower().split(' ', 1)    #Transforma tudo em minusculo e divide no primeiro espaço
            if pesquisa[0] == 'player':         #Se a primeira palavra for player
                prefix = str(pesquisa[1]).lower()#Salva o prefixo do nome
                pesquisaNomes(tabelaHashJogador,raizTrie,prefix)

            elif pesquisa[0] == 'user':         #Se a primeira palavra for user
                idUser = int(pesquisa[1])       #Salva o ID pesquisado
                pesquisaUser(tabelaHashUsuario, tabelaHashJogador, idUser)

            elif pesquisa[0] == 'tags':         #Se a primeira palavra for tags
                tags = pesquisa[1]              #Salva as tags
                buscarTags(tabelaHashTags, tabelaHashJogador, tags)

            elif len(pesquisa[0]) > 3:          #Se tiver mais de 3 letras
                if pesquisa[0][0] == 't' and pesquisa[0][1] == 'o' and pesquisa[0][2] == 'p': #Se começar com top
                    quantidade = int(pesquisa[0].split('p')[1]) #Pega a quantidade do top
                    posicao = pesquisa[1]       #Pega a posição
                    pesquisaPosicao(tabelaHashPosicoes, tabelaHashJogador, posicao, quantidade)

            else:       #Se nao for nenhuma das opções acima
                print("Utilize as consultas player, user, top** ou tags!")

        elif entrada == 3:
            print("\nPrograma Encerrado!\n")

        else:
            print("Digite um numero entre 1 e 3!")

main()

