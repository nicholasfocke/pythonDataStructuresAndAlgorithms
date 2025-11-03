class Grafo:
    def __init__(self):
        self.vertices = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def adicionar_aresta(self, origem, destino):
        if origem in self.vertices and destino in self.vertices:
            self.vertices[origem].append(destino)
            self.vertices[destino].append(origem)  # Para grafos não direcionados

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

    def exibir(self):
        print("Grafo:")
        for vertice, adjacentes in self.vertices.items():
            print(f"{vertice}: {', '.join(map(str, adjacentes))}")

if __name__ == "__main__":
    grafo = Grafo()

    grafo.adicionar_vertice("A")
    grafo.adicionar_vertice("B")
    grafo.adicionar_vertice("C")
    grafo.adicionar_vertice("D")
    grafo.adicionar_vertice("E")

    grafo.adicionar_aresta("A", "B")
    grafo.adicionar_aresta("A", "C")
    grafo.adicionar_aresta("B", "D")
    grafo.adicionar_aresta("C", "E")
    grafo.exibir()

    grafo.bfs("A")
