class Jogador:
    def __init__(self, id, nome, positions):
        self.id = id    #Salva ID do jogador
        self.nome = nome    #Salva nome do jogador
        self.positions = positions      #Salva posições do jogador
        self.soma = 0           #Salva a soma de todas avaliações
        self.qtd = 0            #Salva a qtd total de avaliações

'''
#Não utilizado
class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho      
        self.hash = [None] * tamanho
'''

class Usuario:
    def __init__(self, usuarioId):  
        self.id = usuarioId         #Salva o ID do usuario
        self.avaliacoes = []        #Salva uma lista com as avaliações

class Avaliacao:
    def __init__(self, idJogador, notaJogador):
        self.idJogador = idJogador          #Salva o ID do jogador que foi avaliado
        self.notaJogador = notaJogador      #Salva a nota da avaliação

def hash(id, tamanho):      #Função de Hash
    return id % tamanho 