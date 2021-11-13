from classes import *

#Recebe uma lista, uma tabela hash e um id de usuario
def pesquisaUser(tabelaHashUsuario, TabelaHashJogador, idUser):
    j = 0
    hashUser = hash(idUser, 524287)
    if tabelaHashUsuario[hashUser]:     #Se existe algum elemento nessa posição hash
        for i in range(len(tabelaHashUsuario[hashUser])):      #Percorre a lista de usuarios
            if tabelaHashUsuario[hashUser][i].id == idUser:            #Se encontrou o ID
                ordenar(tabelaHashUsuario[hashUser][i].avaliacoes)    #Ordena a lista dos ids do maior rating

                #Imprime cabeçalho da tabela
                print ("\n{:<15} {:<40} {:<15} {:<15} {:<15}".format('Fifa ID','Name','Global Rating', 'Count', 'Rating'))

                while j < 20 and j < len(tabelaHashUsuario[hashUser][i].avaliacoes):   #Imprime os 20 primeiros ou menos
                    idJogador, notaJogador = buscaListaAvaliacoes(tabelaHashUsuario[hashUser][i], j)   #Pega o ID e a nota da avaliação
                    hashJogador = hash(idJogador, 131071) #Calcula a posição hash
                    nomeJogador, somaJogador, qtdJogador = buscaJogadores(TabelaHashJogador, hashJogador, idJogador)
                    global_rating = somaJogador / qtdJogador    #Faz a média global das avaliações

                    #Imprime em formato de tabela
                    print("{:<15} {:<40} {:<15.6} {:<15} {:<15}".format(idJogador, nomeJogador, global_rating, qtdJogador, notaJogador))
                    j+=1


                return  #Retorna depois de imprimir as 20 avaliações 

        #Se percorreu a lista e não encontrou o usuario
        print("\nUser não encontrado!")   
        return
    else:
        print("\nUser não encontrado!")
        return


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


def ordenar(listaIds):
    ordemCiura = [1,4,10,23,57,132,301,701,1577,3548,7983,17961,40412,90927,204585,460316,1035711]
    shellSort(listaIds, ordemCiura)  #Aplica o Shell Sort na lista de ids

def shellSort(vetor, ordem):
    #Procura a posição no vetor dos tamanhos de segmentos
    for j in range(0, len(ordem), 1):
        if ordem[j] >= len(vetor):
            posicaoOrdem = j-1
            break
    
    #Chama a função de Inserção Direta passando o tamanho do incremento de segmento
    for j in range(posicaoOrdem, -1, -1):
        h = ordem[j]
        insDiretaShellSort(vetor, h)


def insDiretaShellSort(vetor, h):
    for i in range(h, len(vetor), 1):
        chave = vetor[i]
        j = i - h

        #Ordena conforme o rating do id do jogador
        while(j >= 0 and chave.notaJogador > vetor[j].notaJogador):
            vetor[j+h] = vetor[j]
            j -= h
        
        vetor[j + h] = chave


