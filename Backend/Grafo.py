class Grafo:
    def __init__(self):
        self.vertices = {}
    
    def adicionar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []
    
    def adicionar_aresta(self, origem, destino, peso):
        self.adicionar_vertice(origem)
        self.adicionar_vertice(destino)
        self.vertices[origem].append((destino, peso))
        self.vertices[destino].append((origem, peso))  # Grafo não direcionado

    def __str__(self):
        return str(self.vertices)