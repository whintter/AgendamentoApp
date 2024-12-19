#-Pesquisa e Ordenação:
#Método para buscar um serviço pelo nome.
#Método para ordenar serviços pelo valor.

#-Listas Ligadas:
#Estrutura para gerenciar agendamentos temporários.

#-Fila:
#Organização de clientes na ordem de atendimento.

#-Árvore Binária:
#Busca de clientes de forma eficiente.

from collections import deque

# 1. Análise de Complexidade em Pesquisa e Ordenação
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

# 2. Uso de Listas Ligadas
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

# Exemplo de uso para gerenciar agendamentos temporários
lista_agendamentos = ListaLigada()
lista_agendamentos.adicionar({"cliente": "João", "data": "2024-12-20", "hora": "14:00"})
lista_agendamentos.adicionar({"cliente": "Maria", "data": "2024-12-20", "hora": "15:00"})

# 3. Fila para Controle de Atendimentos Pendentes
class FilaAtendimentos:
    def __init__(self):
        self.fila = deque()

    def adicionar_cliente(self, cliente):
        self.fila.append(cliente)

    def atender_cliente(self):
        if self.fila:
            return self.fila.popleft()
        return None

    def listar_fila(self):
        return list(self.fila)

# Exemplo de uso para fila de atendimentos
fila_atendimentos = FilaAtendimentos()
fila_atendimentos.adicionar_cliente("João")
fila_atendimentos.adicionar_cliente("Maria")
atendido = fila_atendimentos.atender_cliente()

# 4. Árvore Binária para Busca de Clientes
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

# Exemplo de uso para busca de clientes
arvore_clientes = ArvoreBinaria()
arvore_clientes.inserir("joao", {"nome": "João", "telefone": "123456789"})
arvore_clientes.inserir("maria", {"nome": "Maria", "telefone": "987654321"})
cliente_encontrado = arvore_clientes.buscar("joao")

# Saídas de exemplo
print("Lista de agendamentos temporários:", lista_agendamentos.listar())
print("Fila de atendimentos após primeiro cliente atendido:", fila_atendimentos.listar_fila())
print("Cliente encontrado na árvore binária:", cliente_encontrado.cliente if cliente_encontrado else "Não encontrado")


#Importe as classes e funções necessárias nas páginas que a gente for usar. exemplo:
#from estruturas import ServicoHelper, ListaLigada, FilaAtendimentos, ArvoreBinaria