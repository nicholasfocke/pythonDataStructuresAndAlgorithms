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

    def dfs(self, inicio, visitados=None):
        if inicio not in self.vertices:
            print("Vértice inicial não encontrado no grafo.")
            return

        if visitados is None:
            visitados = set()

        print(inicio, end=" ")
        visitados.add(inicio)

        for vizinho in self.vertices[inicio]:
            if vizinho not in visitados:
                self.dfs(vizinho, visitados)

    def exibir(self):
        if not self.vertices:
            print("Grafo vazio!!")
            return

        print("Grafo:")
        for vertice, adjacentes in self.vertices.items():
            print(f"{vertice}: {', '.join(map(str, adjacentes))}")

if __name__ == "__main__":
    grafo = Grafo()

    grafo.exibir()
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

    print("\nBusca em profundidade (DFS):")
    grafo.dfs("A")
