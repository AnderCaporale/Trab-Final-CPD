from classeTrie import *
from classes import *

def pesquisaNomes(TabelaHashJogador,raizTrie:Trie,planilha,prefix):
    resultados = raizTrie.busca(prefix)
    # Imprime cabeçalho da tabela
    print("{:<15} {:<40} {:<25} {:<15} {:<15}".format('Fifa ID', 'Name', 'Positions', 'Rating', 'Count'))
    for resultado in resultados:
        id = planilha['sofifa_id'][resultado]
        hashJogador = hash(id, 131071)  # Faz o hash do id
        for i in range(len(TabelaHashJogador[hashJogador])):  # Trata colisoes na tabela hash
            if TabelaHashJogador[hashJogador][i].id == id:  # Se encontrou o jogador
                if TabelaHashJogador[hashJogador][i].qtd == 0: # Se não houver avaliacao sobre esse jogador
                    rating = '-' #simbolo de sem rating, rating desconhecido
                else:
                    rating = TabelaHashJogador[hashJogador][i].soma / TabelaHashJogador[hashJogador][i].qtd
                print("{:<15} {:<40} {:<25} {:<15.6} {:<15}".format(TabelaHashJogador[hashJogador][i].id,
                                                                    TabelaHashJogador[hashJogador][i].nome, (TabelaHashJogador[hashJogador][i].positions),
                                                                    rating,
                                                                    TabelaHashJogador[hashJogador][i].qtd))  # Imprime a tabela

