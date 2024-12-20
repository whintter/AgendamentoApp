
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


class NoArvore:
    def __init__(self, servico):
        self.servico = servico
        self.esquerda = None
        self.direita = None


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def adicionar(self, servico):
        novo_no = NoArvore(servico)
        if self.raiz is None:
            self.raiz = novo_no
        else:
            self._adicionar_recursivo(self.raiz, novo_no)

    def _adicionar_recursivo(self, atual, novo_no):
        if novo_no.servico['nome'] < atual.servico['nome']:
            if atual.esquerda is None:
                atual.esquerda = novo_no
            else:
                self._adicionar_recursivo(atual.esquerda, novo_no)
        else:
            if atual.direita is None:
                atual.direita = novo_no
            else:
                self._adicionar_recursivo(atual.direita, novo_no)

    def buscar(self, nome):
        return self._buscar_recursivo(self.raiz, nome)

    def _buscar_recursivo(self, atual, nome):
        if atual is None:
            return None
        if atual.servico['nome'] == nome:
            return atual.servico
        if nome < atual.servico['nome']:
            return self._buscar_recursivo(atual.esquerda, nome)
        return self._buscar_recursivo(atual.direita, nome)

    def listar_ordenado(self):
        servicos = []
        self._in_order(self.raiz, servicos)
        return servicos

    def _in_order(self, atual, servicos):
        if atual is not None:
            self._in_order(atual.esquerda, servicos)
            servicos.append(atual.servico)
            self._in_order(atual.direita, servicos)
