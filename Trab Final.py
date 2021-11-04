import pandas as pd
from time import perf_counter
from menu import *
from carregar import *
from classes import *
from funcao2 import *

def main():
    planilhaPlayer = pd.read_csv("players.csv", delimiter = ",") #Le a planilha
    planilhaRating = pd.read_csv("minirating.csv", delimiter = ",") #Le a planilha
    TabelaHashJogador = [None] * 131071 
    TabelaHashUsuario = [None] * 524287  

    inicioTimer = perf_counter()
    carregar_players(TabelaHashJogador, planilhaPlayer)
    fimTimer = perf_counter()
    print(f"Tempo: {fimTimer - inicioTimer} segundos")

    inicioTimer = perf_counter()
    carregar_rating(TabelaHashJogador, TabelaHashUsuario, planilhaRating)
    fimTimer = perf_counter()
    print(f"Tempo: {fimTimer - inicioTimer} segundos")

    entrada = 0
    #Fica no loop até a entrada ser a opção 6
    while entrada != 5:
        entrada = menu()

        if entrada == 1:
            pass
            #funcao1()
        elif entrada == 2:
            idUser = int(input('Informe o id do Usuario: '))
            i = hash(idUser, 524287)
            print()
            pesquisaUser(TabelaHashUsuario[i], TabelaHashJogador, idUser)
            
        elif entrada == 3:
            pass
            #funcao3()

        elif entrada == 4:
            pass
            #funcao4()
        else:
            print("Programa Encerrado!")

main()

