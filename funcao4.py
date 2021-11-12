from classes import *
from funcao3 import ordenar

def buscarTags(TabelaHashTags, TabelaHashJogador, tags):
    vetorTags = tags.split("' ")
    vetorIds = []
    for i in range(len(vetorTags)):
        vetorTags[i] = vetorTags[i].replace("'", "")

    for i in range(len(vetorTags)):
        h = hash_palavras(vetorTags[i], 7001)

        for j in range(len(TabelaHashTags[h])):
            if TabelaHashTags[h][j].nome == vetorTags[i]: 
                vetorIds.append(TabelaHashTags[h][j].ids)


    vetorIds = verifica_interseccao(vetorIds)
    ordenar(vetorIds, TabelaHashJogador)    #Ordena a lista dos ids do maior rating
    print ("{:<15} {:<50} {:<25} {:<15} {:<15}".format('Fifa ID','Name','Positions', 'Rating', 'Count'))

    for i in range(len(vetorIds)):
        hashJogador = hash(vetorIds[i], 131071)     #Faz o hash do id

        for j in range(len(TabelaHashJogador[hashJogador])):      #Trata colisoes na tabela hash
            if TabelaHashJogador[hashJogador][j].id == vetorIds[i]: #Se encontrou o jogador
                print ("{:<15} {:<50} {:<25} {:<15.7} {:<15}".format(TabelaHashJogador[hashJogador][j].id, TabelaHashJogador[hashJogador][j].nome, ', '.join(TabelaHashJogador[hashJogador][j].positions), TabelaHashJogador[hashJogador][j].soma / TabelaHashJogador[hashJogador][j].qtd, TabelaHashJogador[hashJogador][j].qtd))  #Imprime a tabela



def verifica_interseccao(matrizIDs):
    vetorIntersec = []      

    for i in range(len(matrizIDs)):         #Percorre a matriz
        for j in range(len(matrizIDs[i])):      
            idBusca = matrizIDs[i][j]       #Testa elemento a elemento da matriz
            achou = 1               #Contador
            for k in range(i+1, len(matrizIDs)):    #Compara o elemento com as outras linhas
                for l in range(len(matrizIDs[k])):  #Compara com cada elemento das outras linhas
                    if idBusca == matrizIDs[k][l]:  #Se achou repetido
                        achou += 1                  #Incrementa contador
                        break                       #Pula para comparar com a proxima linha 
                if achou != k+1:                    #Se não encontrou em alguma linha, para a busca desse elemento
                    break 
            #Se contador é igual ao numero de linhas, o numero ta em todas as linhas    
            if achou == len(matrizIDs):             
                vetorIntersec.append(idBusca)       #Salva o id igual em todas as linhas

    return vetorIntersec

