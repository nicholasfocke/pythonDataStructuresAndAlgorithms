class Grafo:
    def __init__(self):
        self.vertices = {}
    
    def adicionar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []
    
    def adicionar_aresta(self, origem, destino):
        if origem in self.vertices and destino in self.vertices:
            self.vertices[origem].append(destino)
            self.vertices[destino].append(origem)
    
    def exibir(self):
        if not self.vertices:
            print('Grafo vazio!')
            return
        
        print('Grafo:')
        for vertice, adjacentes in self.vertices.items():
            print(f'{vertice}: {','.join(map(str, adjacentes))}')
        
    def existe_conexao(self, origem, destino):
        if origem in self.vertices and destino in self.vertices:
            if destino in self.vertices[origem]:
                print('Existe conexão!')
                return True
            else:
                print('Não existe conexão!')
                return False
        else:
            print('Um ou ambos vertices digitados não existem!')
            return False
    
    def remover_vertice(self, vertice):
        if vertice in self.vertices:
            for adjacentes in self.vertices.values():
                if vertice in adjacentes:
                    adjacentes.remove(vertice)
            del self.vertices[vertice]
            print(f'vertice {vertice} removido')
        else:
            print(f'O vertice {vertice} não existe no Grafo')
    
    def dfs(self, inicio, visitados=None):
        if inicio not in self.vertices:
            print('Vertice digitado não existe no grafo!')
            return
        
        if visitados is None:
            visitados = set()
        
        print(inicio, end=' ')
        visitados.add(inicio)

        for vizinho in self.vertices[inicio]:
            if vizinho not in visitados:
                self.dfs(vizinho, visitados)
    
    def bfs(self, inicio):
        if inicio not in self.vertices:
            print('Vertice digitado não existe no grafo!')
            return
        
        visitados = set()
        fila = [inicio]

        print('Busca em largura (BFS): ')
        while fila:
            vertice = fila.pop(0)
            if vertice not in visitados:
                print(vertice, end=' ')
                visitados.add(vertice)
                fila.extend([v for v in self.vertices[vertice] if v not in visitados])
        print()
    
    def exibir_vizinhos(self, vertice):
        if vertice in self.vertices:
            vizinho = self.vertices[vertice]
            if vizinho:
                print(f'{vertice}: {','.join(map(str, vizinho))}')
            else:
                print('O vértice não possui vizinhos')
        else:
            print('Vértice não existe no Grafo!')