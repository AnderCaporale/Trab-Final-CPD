from classes import *
from funcao3 import ordenar

def buscarTags(TabelaHashTags, TabelaHashJogador, tags):

    vetorTags = tags.split("' ")        #Coloca as tags em um vetor
    vetorIds = []
    for i in range(len(vetorTags)):     #Retira as aspas das tags
        vetorTags[i] = vetorTags[i].replace("'", "")

    for i in range(len(vetorTags)):     #Percorre o vetor de tags de entrada
        h = hash_palavras(vetorTags[i], tamanho_tabelaHashTags)   #Faz o hash para cada tag
        if TabelaHashTags[h]:   #Se existe algum elemento nessa posição hash
            for j in range(len(TabelaHashTags[h])): #Percorre a lista de tags
                if TabelaHashTags[h][j].nome == vetorTags[i]:   #Se encontrou a tag
                    vetorIds.append(TabelaHashTags[h][j].ids)   #Adiciona na matriz de tags
                    
            #Se o tamanho é menor do que o i, é porque não fez o append, portanto não encontrou a tag
            if len(vetorIds) < i:           
                print(f"\nTag '{vetorTags[i]}' não encontradaa!")
                return 
        else:
            print(f"\nTag '{vetorTags[i]}' não encontrada!")
            return

    vetorIds = verifica_interseccao(vetorIds)       #Verifica quais IDs estão nas tags solicitadas
    ordenar(vetorIds, TabelaHashJogador)            #Ordena a lista dos ids do maior rating
    print ("{:<15} {:<50} {:<25} {:<15} {:<15}".format('Fifa ID','Name','Positions', 'Rating', 'Count'))

    for i in range(len(vetorIds)):                  #Percorre a lista de vetores
        hashJogador = hash(vetorIds[i], tamanho_tabelaHashJogador)     #Faz o hash do id

        for j in range(len(TabelaHashJogador[hashJogador])):      #Trata colisoes na tabela hash
            if TabelaHashJogador[hashJogador][j].id == vetorIds[i]: #Se encontrou o jogador
                rating = TabelaHashJogador[hashJogador][j].soma / TabelaHashJogador[hashJogador][j].qtd if TabelaHashJogador[hashJogador][j].qtd != 0 else 0.0
                
                print ("{:<15} {:<50} {:<25} {:<15.7} {:<15}".format(TabelaHashJogador[hashJogador][j].id, TabelaHashJogador[hashJogador][j].nome, ', '.join(TabelaHashJogador[hashJogador][j].positions), rating, TabelaHashJogador[hashJogador][j].qtd))  #Imprime a tabela
                break

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

