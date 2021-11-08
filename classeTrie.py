class Trie:
    class NodoTrie:
        def __init__(self):
            self.filhos = [None] * 256  #TODO na versão clean tem menos do que todoas ascii, modificar depois
            # numero_fim_nome = None se não for final de nome e >=0 se for final de nome
            # esse numero de fim de nome também vai ser usado pra achar o jogador na tabela csv de players_clean2
            self.numero_fim_nome = None


    def __init__(self):
        """quando instanciada a raiz recebe um nodo vazio basicamente(filhos dele não tem nada)"""
        self.raiz = Trie.NodoTrie()


    def __char_para_numero(self,letra):
        """transforma as letras em posicoes do vetor de filhos de cada nodo"""
        return ord(letra)#TODO modificar depois pra aceitar so as letras da versão clean

    def insere_nodo(self,nome,val):
        """talvez fazer não ser recursiva depois pra ser mais rapido"""
        self.raiz = self.__insere_nodo(self.raiz, nome, val, 0)

    def __insere_nodo(self, nodo:NodoTrie, nome:str, val, d):
        if d == len(nome):
            nodo.numero_fim_nome = val
            return nodo
        n = self.__char_para_numero(nome[d])
        #se não tiver o filho pra essa letra criar um
        if not nodo.filhos[n]:
            nodo.filhos[n] = Trie.NodoTrie()
        nodo.filhos[n] = self.__insere_nodo(nodo.filhos[n],nome,val,d+1)
        return nodo

    def get(self,raiz,prefix):
        """retorna None se não tem esse prefixo, retorno o nodo do prefixo se tem ele"""
        nodo = raiz
        tamanho = len(prefix)
        for i in range(tamanho):
            index = self.__char_para_numero(prefix[i])
            # se nao tiver o filho naquele index
            if not nodo.filhos[index]:
                return None
            nodo = nodo.filhos[index]
        return nodo

    def __busca(self,nodo,resultados):
        for filho in nodo.filhos:
            if filho is not None:
                if filho.numero_fim_nome is not None:
                    resultados.append(filho.numero_fim_nome)
                self.__busca(filho, resultados)
        return nodo

    def busca(self,prefix:str):
        """retorna None se não achar, retorna lista de numero_fim_nome de todos nomes com esse prefixo se achar"""
        nodo = self.raiz
        nodo = self.get(nodo,prefix)
        resultados = []
        if nodo is not None:
            self.__busca(nodo,resultados)
        return resultados




