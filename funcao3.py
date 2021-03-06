from classes import *

def pesquisaPosicao(TabelaHashPosicoes, TabelaHashJogador, posicao, quantidade):
    h = hash_palavras(posicao, tamanho_tabelaHashPosicoes)    #Faz o hash da posicao do jogador

    if TabelaHashPosicoes[h]:       #Se existe algum elemento nessa posição hash
        #Imprime Cabeçalho da tabela
        print ("\n{:<15} {:<50} {:<25} {:<15} {:<15}".format('Fifa ID','Name','Positions', 'Rating', 'Count'))
        for j in range(len(TabelaHashPosicoes[h])): #Trata colisoes na tabela hash
            if TabelaHashPosicoes[h][j].nome == posicao:    #Se encontrou posição
                
                ordenar(TabelaHashPosicoes[h][j].ids, TabelaHashJogador)    #Ordena a lista dos ids do maior rating para o menor
                for i in range(quantidade):     #Repete conforme as vezes solicitadas
                    if i < len(TabelaHashPosicoes[h][j].ids):   #Verifica se foi solicitado um ranking maior que a qtd de jogadores
                        hashJogador = hash(TabelaHashPosicoes[h][j].ids[i], tamanho_tabelaHashJogador)     #Faz o hash do id
                        for k in range(len(TabelaHashJogador[hashJogador])):      #Trata colisoes na tabela hash
                            if TabelaHashJogador[hashJogador][k].id == TabelaHashPosicoes[h][j].ids[i]: #Se encontrou o jogador
                                if TabelaHashJogador[hashJogador][k].qtd >= 1000:   #Se tem mais de 1000 avaliacoes
                                    rating = TabelaHashJogador[hashJogador][k].soma / TabelaHashJogador[hashJogador][k].qtd if TabelaHashJogador[hashJogador][k].qtd != 0 else 0.0

                                    print ("{:<15} {:<50} {:<25} {:<15.7} {:<15}".format(TabelaHashJogador[hashJogador][k].id, TabelaHashJogador[hashJogador][k].nome, ', '.join(TabelaHashJogador[hashJogador][k].positions), rating, TabelaHashJogador[hashJogador][k].qtd))  #Imprime a tabela

                return  #Retorna depois de imprimir a quantidade de avaliações solicitadas

        #Se percorreu a lista e não encontrou a posição solicitada
        print("\nPosição não encontrada!")   
        return
    else:
        print("\nPosição não encontrada!")
        return

def ordenar(listaIds, TabelaHashJogador):
    ordemCiura = [1,4,10,23,57,132,301,701,1577,3548,7983,17961,40412,90927,204585,460316,1035711]
    shellSort(listaIds, ordemCiura, TabelaHashJogador)  #Aplica o Shell Sort na lista de ids

def shellSort(vetor, ordem, TabelaHashJogador):
    #Procura a posição no vetor dos tamanhos de segmentos
    for j in range(0, len(ordem), 1):
        if ordem[j] >= len(vetor):
            posicaoOrdem = j-1
            break
    
    #Chama a função de Inserção Direta passando o tamanho do incremento de segmento
    for j in range(posicaoOrdem, -1, -1):
        h = ordem[j]
        insDiretaShellSort(vetor, h, TabelaHashJogador)


def insDiretaShellSort(vetor, h, TabelaHashJogador):
    for i in range(h, len(vetor), 1):
        chave = vetor[i]
        j = i - h

        #Ordena conforme o rating do id do jogador
        while(j >= 0 and acharRating(chave, TabelaHashJogador) > acharRating(vetor[j], TabelaHashJogador)):
            vetor[j+h] = vetor[j]
            j -= h
        
        vetor[j + h] = chave


def acharRating(idJogador, TabelaHashJogador):
    h = hash(idJogador, tamanho_tabelaHashJogador)     #Faz o hash
    for i in range(len(TabelaHashJogador[h])):  #Trata colisoes
        if TabelaHashJogador[h][i].id == idJogador: #Se encontrou o id
            rating = TabelaHashJogador[h][i].soma / TabelaHashJogador[h][i].qtd if TabelaHashJogador[h][i].qtd != 0 else 0.0
            return rating
            

    