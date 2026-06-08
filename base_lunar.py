"""
GS - DYNAMIC PROGRAMMING
Projeto: ARTEMIS-LOG - Gerenciador de Suprimentos da Base Lunar
--------------------------------------------------------------------
Tema (Kick-off da GS): Economia Espacial / Logística em Base Lunar
"""

import heapq  # módulo para fila de prioridade (heap)


class FilaCargueiros:
    def __init__(self):
        """Cria uma fila vazia para os cargueiros."""
        self.fila = []

    def adicionar(self, cargueiro):
        """Adiciona um cargueiro no final da fila."""
        self.fila.append(cargueiro)
        print(f"Cargueiro '{cargueiro}' entrou na fila de descarga.")

    def atender(self):
        """Atende o primeiro cargueiro da fila (FIFO)."""
        if self.fila:
            atendido = self.fila.pop(0)
            print(f"Descarregando cargueiro: {atendido}")
            return atendido
        else:
            print("Fila vazia, nenhum cargueiro para descarregar.")
            return None

    def mostrar(self):
        """Mostra todos os cargueiros que ainda estão na fila."""
        if self.fila:
            print(f"Fila atual: {self.fila}")
        else:
            print("Fila vazia.")

    def is_empty(self):
        """Verifica se a fila está vazia."""
        return len(self.fila) == 0


class PilhaOperacoes:
    def __init__(self):
        """Cria uma pilha vazia para guardar as operações."""
        self.pilha = []

    def push(self, operacao):
        """Empilha uma nova operação no topo."""
        self.pilha.append(operacao)
        print(f"Operação registrada: {operacao}")

    def pop(self):
        """Desempilha a última operação (desfazer)."""
        if not self.is_empty():
            desfeita = self.pilha.pop()
            print(f"Desfazendo operação: {desfeita}")
            return desfeita
        else:
            print("Pilha vazia, nada para desfazer.")
            return None

    def peek(self):
        """Mostra a operação do topo sem remover."""
        if not self.is_empty():
            return self.pilha[-1]
        return "Pilha vazia"

    def is_empty(self):
        """Verifica se a pilha está vazia."""
        return len(self.pilha) == 0

    def mostrar(self):
        """Mostra todas as operações da pilha."""
        if self.pilha:
            print(f"Pilha atual: {self.pilha}")
        else:
            print("Pilha vazia.")



class FilaPrioridade:
    def __init__(self):
        """Cria uma fila de prioridade vazia."""
        self.fila = []

    def adicionar(self, urgencia, pedido):
        """Adiciona um pedido no heap (urgência, pedido)."""
        heapq.heappush(self.fila, (urgencia, pedido))
        print(f"Pedido '{pedido}' adicionado | Urgência: {urgencia}")

    def atender(self):
        """Atende o pedido de maior prioridade (menor número)."""
        if self.fila:
            urgencia, pedido = heapq.heappop(self.fila)
            print(f"Atendendo: {pedido} | Urgência: {urgencia}")
            return pedido
        else:
            print("Não há pedidos para atender.")
            return None

    def mostrar(self):
        """Mostra todos os pedidos da fila."""
        if self.fila:
            print("Pedidos na fila:")
            for urgencia, pedido in sorted(self.fila):
                print(f"  - {pedido} (urgência {urgencia})")
        else:
            print("Fila vazia.")



class GrafoBase:
    def __init__(self):
        """Cria um grafo vazio (dicionário de adjacência)."""
        self.grafo = {}

    def adicionar_modulo(self, nome):
        """Adiciona um módulo (nó) na base."""
        if nome not in self.grafo:
            self.grafo[nome] = []

    def adicionar_rota(self, origem, destino, custo):
        """Adiciona uma rota bidirecional entre dois módulos."""
        self.adicionar_modulo(origem)
        self.adicionar_modulo(destino)
        self.grafo[origem].append((destino, custo))
        self.grafo[destino].append((origem, custo))

    def menor_rota(self, origem, destino):

        distancias = {no: float("inf") for no in self.grafo}
        anteriores = {no: None for no in self.grafo}
        distancias[origem] = 0

        fila = [(0, origem)]

        while fila:
            custo_atual, no_atual = heapq.heappop(fila)

            if custo_atual > distancias[no_atual]:
                continue

            for vizinho, peso in self.grafo[no_atual]:
                novo_custo = custo_atual + peso
                if novo_custo < distancias[vizinho]:
                    distancias[vizinho] = novo_custo
                    anteriores[vizinho] = no_atual
                    heapq.heappush(fila, (novo_custo, vizinho))

        
        pilha = []
        atual = destino
        while atual is not None:
            pilha.append(atual)
            atual = anteriores[atual]

        
        caminho = []
        while pilha:
            caminho.append(pilha.pop())

        return caminho, distancias[destino]

    def mostrar(self):
        """Mostra todos os módulos e suas conexões."""
        print(f"Total de módulos: {len(self.grafo)}")
        total_rotas = sum(len(v) for v in self.grafo.values()) // 2
        print(f"Total de rotas: {total_rotas}")



def montar_base_lunar():
    """Cria o grafo da base lunar com 18 módulos e 30 rotas."""
    base = GrafoBase()

    
    rotas = [
        ("PP",   "DEP",   4),   
        ("PP",   "GAR",   3), 
        ("PP",   "OFI",   6),   
        ("DEP",  "HAB1",  5),  
        ("DEP",  "HAB2",  7),   
        ("DEP",  "EST",   6),   
        ("DEP",  "LAB",   8), 
        ("DEP",  "MED",   9),   
        ("GAR",  "OFI",   2),   
        ("GAR",  "MIN",  10),
        ("OFI",  "FAB",   3),  
        ("FAB",  "LAB",   4),   
        ("FAB",  "MIN",   6),   
        ("MIN",  "AGU",   5),   
        ("AGU",  "RES",   3), 
        ("RES",  "EST",   4),  
        ("RES",  "HAB1",  5),   
        ("RES",  "HAB2",  6), 
        ("OXI",  "HAB1",  4),   
        ("OXI",  "HAB2",  5),   
        ("OXI",  "EST",   3),   
        ("ENE",  "OXI",   2),   
        ("ENE",  "COM",   3),   
        ("ENE",  "HAB1",  6),  
        ("ENE",  "HAB2",  6),  
        ("COM",  "OBS",   4),   
        ("COM",  "LAB",   5),   
        ("HAB1", "MED",   2),   
        ("HAB2", "MED",   3),   
        ("HEL",  "MED",   3), 
    ]

    for origem, destino, custo in rotas:
        base.adicionar_rota(origem, destino, custo)

    return base



def menu():
    """Menu principal do sistema ARTEMIS-LOG."""
    cargueiros = FilaCargueiros()
    operacoes  = PilhaOperacoes()
    pedidos    = FilaPrioridade()
    base       = montar_base_lunar()

    print("=" * 60)
    print(" ARTEMIS-LOG - Gerenciador da Base Lunar (GS)")
    print("=" * 60)
    base.mostrar()
    print("=" * 60)

    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1 - Cargueiros: adicionar/descarregar")
        print("2 - Operações do rover: registrar/desfazer")
        print("3 - Pedidos urgentes: adicionar/atender")
        print("4 - Calcular rota entre dois módulos")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        # OPÇÃO 1: FIFO
        if opcao == "1":
            sub = input("  a-Adicionar | b-Descarregar | c-Mostrar fila: ")
            if sub == "a":
                nome = input("  Nome do cargueiro: ")
                cargueiros.adicionar(nome)
            elif sub == "b":
                cargueiros.atender()
            elif sub == "c":
                cargueiros.mostrar()
            else:
                print("  Opção inválida.")

        #  OPÇÃO 2: LIFO
        elif opcao == "2":
            sub = input("  a-Registrar | b-Desfazer | c-Mostrar pilha: ")
            if sub == "a":
                op = input("  Descrição da operação: ")
                operacoes.push(op)
            elif sub == "b":
                operacoes.pop()
            elif sub == "c":
                operacoes.mostrar()
            else:
                print("  Opção inválida.")

        # OPÇÃO 3: HEAP (prioridade) 
        elif opcao == "3":
            sub = input("  a-Adicionar | b-Atender | c-Mostrar fila: ")
            if sub == "a":
                pedido = input("  Descrição do pedido: ")
                try:
                    urg = int(input("  Urgência (1=máxima, 5=mínima): "))
                    pedidos.adicionar(urg, pedido)
                except ValueError:
                    print("  Urgência precisa ser um número.")
            elif sub == "b":
                pedidos.atender()
            elif sub == "c":
                pedidos.mostrar()
            else:
                print("  Opção inválida.")

        #  OPÇÃO 4: GRAFO (Dijkstra) 
        elif opcao == "4":
            print("  Módulos disponíveis:")
            print("  PP, DEP, HAB1, HAB2, LAB, EST, OXI, AGU, ENE,")
            print("  COM, MED, OFI, MIN, FAB, HEL, OBS, RES, GAR")
            origem  = input("  Módulo de ORIGEM: ").upper()
            destino = input("  Módulo de DESTINO: ").upper()
            if origem in base.grafo and destino in base.grafo:
                caminho, custo = base.menor_rota(origem, destino)
                print(f"  Rota ótima: {' -> '.join(caminho)}")
                print(f"  Custo total: {custo}")
            else:
                print("  Módulo não encontrado. Verifique os nomes.")

        # OPÇÃO 5: SAIR 
        elif opcao == "5":
            print("Encerrando ARTEMIS-LOG. Até a próxima missão!")
            break

        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    menu()
