class Grafo:
    def __init__(self):
        self.vertices = {}
    
    def adicionar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []
    
    def adicionar_aresta(self, origem, destino):
        if origem in self.vertices and destino in self.vertices:
            self.vertices[origem].append(destino)
            self.vertices[destino].append(origem) #para grafos não direcionados
    
    def tamanho_grafo(self):
        print(f'Tamanho do grafo: {len(self.vertices)} vértices')

    def exibir(self):
        if not self.vertices:
            print("Grafo vazio!!")
            return
        
        print('Grafo: ')
        for vertice, adjacentes in self.vertices.items():
            print(f'{vertice}: {','.join(map(str, adjacentes))}')

    def contar_arestas(self):
        total_arestas = sum(len(adjacentes) for adjacentes in self.vertices.values()) // 2
        print('Número total de arestas:', total_arestas)

    def encontrar_vertices_isolados(self):
        isolados = [vertice for vertice, adjacentes in self.vertices.items() if not adjacentes]
        print('Vértices isolados:', ', '.join(isolados) if isolados else 'Nenhum vértice isolado encontrado.')

    def remover_vertice(self, vertice):
        if vertice in self.vertices:
            for adjacentes in self.vertices.values():
                if vertice in adjacentes:
                    adjacentes.remove(vertice)
            del self.vertices[vertice]
            print(f'Vertice {vertice} removido.')
        else:
            print(f'Vertice {vertice} não existe no grafo.')

    def remover_aresta(self, origem, destino):
        if origem in self.vertices and destino in self.vertices:
            if destino in self.vertices[origem]:
                self.vertices[origem].remove(destino)
            if origem in self.vertices[destino]:
                self.vertices[destino].remove(origem)
            print(f'Aresta entre {origem} e {destino} removida.')
        else:
            print('Uma ou ambas as extremidades da aresta não existem no grafo.')

    def existe_conexao(self, origem, destino):
        if origem in self.vertices and destino in self.vertices:
            if destino in self.vertices[origem]:
                print(f'Existe uma conexão entre {origem} e {destino}.')
                return True
            else:
                print(f'Não existe uma conexão entre {origem} e {destino}.')
                return False
        else:
            print('Um ou ambos os vértices não existem no grafo.')
            return False

    def dfs(self, inicio, visitados=None, primeira_chamada=True):
        if inicio not in self.vertices:
            print("Vértice inicial não encontrado no grafo.")
            return
        
        if visitados is None:
            visitados = set()

        if primeira_chamada:
            print("Busca em profundidade (DFS):")

        print(inicio, end=" ")
        visitados.add(inicio)

        for vizinho in self.vertices[inicio]:
            if vizinho not in visitados:
                self.dfs(vizinho, visitados, primeira_chamada=False)

    def bfs(self, inicio):
        if inicio not in self.vertices:
            print("Vértice inicial não encontrado no grafo.")
            return

        visitados = set()
        fila = [inicio]

        print("Busca em largura (BFS):")
        while fila:
            vertice = fila.pop(0)
            if vertice not in visitados:
                print(vertice, end=" ")
                visitados.add(vertice)
                fila.extend([v for v in self.vertices[vertice] if v not in visitados])
        print()

    def exibir_vizinhos(self, vertice):
        if vertice in self.vertices:
            vizinhos = self.vertices[vertice]
            if vizinhos:
                print(f'Vizinhos do vértice {vertice}: {", ".join(vizinhos)}')
            else:
                print(f'O vértice {vertice} não possui vizinhos.')
        else:
            print(f'O vértice {vertice} não existe no grafo.')

if __name__ == '__main__':
    grafo = Grafo()
    grafo.adicionar_vertice('A')
    grafo.adicionar_vertice('B')
    grafo.adicionar_vertice('C')
    grafo.adicionar_vertice('D')
    grafo.adicionar_vertice('E')
    
    grafo.adicionar_aresta('B', 'C')
    grafo.adicionar_aresta('A', 'B')
    grafo.adicionar_aresta('D', 'C')
    grafo.adicionar_aresta('E', 'D')
    grafo.adicionar_aresta('A', 'E')

    grafo.exibir()
    grafo.bfs("A")
    grafo.dfs("A")
    print()
    grafo.tamanho_grafo()
    print()
    grafo.contar_arestas()
    print()
    grafo.encontrar_vertices_isolados()
    print()
    grafo.remover_aresta('A', 'B')
    grafo.exibir()
    print()
    grafo.remover_vertice('C')
    grafo.exibir()
    print()
    grafo.existe_conexao('A', 'E')
    grafo.existe_conexao('A', 'C')
    print()
    grafo.exibir_vizinhos('A')
    grafo.exibir_vizinhos('C')