
from collections import deque

# Análise de Complexidade em Pesquisa e Ordenação
class ServicoHelper:
    @staticmethod
    def buscar_servico_por_nome(lista_servicos, nome):
        """Busca um serviço pelo nome. Complexidade: O(n)"""
        for servico in lista_servicos:
            if servico.nome.lower() == nome.lower():
                return servico
        return None

    @staticmethod
    def ordenar_servicos_por_valor(lista_servicos):
        """Ordena a lista de serviços pelo valor em ordem crescente. Complexidade: O(n log n)"""
        return sorted(lista_servicos, key=lambda servico: servico.valor)

#  Uso de Listas Ligadas
class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaLigada:
    def __init__(self):
        self.cabeca = None

    def adicionar(self, dado):
        novo_no = No(dado)
        if not self.cabeca:
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no

    def listar(self):
        atual = self.cabeca
        elementos = []
        while atual:
            elementos.append(atual.dado)
            atual = atual.proximo
        return elementos

#  Fila 

class FilaAtendimentos:
    def __init__(self):
        self.fila = []

    def adicionar_agendamento(self, agendamento):
        self.fila.append(agendamento)

    def obter_agendamentos(self):
        return self.fila


# Árvore Binária
class NoArvore:
    def __init__(self, chave, cliente):
        self.chave = chave
        self.cliente = cliente
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave, cliente):
        novo_no = NoArvore(chave, cliente)
        if not self.raiz:
            self.raiz = novo_no
        else:
            self._inserir_recursivo(self.raiz, novo_no)

    def _inserir_recursivo(self, atual, novo_no):
        if novo_no.chave < atual.chave:
            if atual.esquerda:
                self._inserir_recursivo(atual.esquerda, novo_no)
            else:
                atual.esquerda = novo_no
        else:
            if atual.direita:
                self._inserir_recursivo(atual.direita, novo_no)
            else:
                atual.direita = novo_no

    def buscar(self, chave):
        return self._buscar_recursivo(self.raiz, chave)

    def _buscar_recursivo(self, atual, chave):
        if not atual or atual.chave == chave:
            return atual
        if chave < atual.chave:
            return self._buscar_recursivo(atual.esquerda, chave)
        return self._buscar_recursivo(atual.direita, chave)
