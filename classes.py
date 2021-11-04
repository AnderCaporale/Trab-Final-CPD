class Jogador:
    def __init__(self, id, nome, positions):
        self.id = id
        self.nome = nome
        self.positions = positions
        self.soma = 0
        self.qtd = 0
        self.next = None

class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.hash = [None] * tamanho

class Usuario:
    def __init__(self, usuarioId):
        self.id = usuarioId
        self.avaliacoes = []
        self.next = None

class Avaliacao:
    def __init__(self, idJogador, notaJogador):
        self.idJogador = idJogador
        self.notaJogador = notaJogador
        self.next = None


def hash(id, tamanho):
    return id % tamanho