class Jogador:
    def __init__(self, id, nome, positions):
        self.id = id    #Salva ID do jogador
        self.nome = nome    #Salva nome do jogador
        self.positions = positions      #Salva posições do jogador
        self.soma = 1           #Salva a soma de todas avaliações
        self.qtd = 1            #Salva a qtd total de avaliações

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

class Posicao:          
    def __init__(self, nome):
        self.nome = nome                #Salva o nome da posição
        self.ids = []                   #Lista para salvar os ids dos jogadores


def hash(id, tamanho):      #Função de Hash
    return id % tamanho 

def hash_palavras(chave, tamanho):              #Função Hash para palavras
    soma = 0
    p = 127
    for i in range(len(chave)):
        soma += ord(chave[i]) * (p**i)
    
    return (soma % tamanho)