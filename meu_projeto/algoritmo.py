class Grafo:
    def __init__(self):
        self.vertices = {}
    
    def adicionar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = {}
    
    def adicionar_aresta(self, origem, destino, peso):
        if origem in self.vertices and destino in self.vertices:
            self.vertices[origem][destino] = peso
            self.vertices[destino][origem] = peso  # Se o grafo for não-direcionado

def dijkstra(grafo, inicio):
    distancias = {vertice: float('infinity') for vertice in grafo.vertices}
    distancias[inicio] = 0
    caminho = {vertice: None for vertice in grafo.vertices}
    vertices_a_visitar = grafo.vertices.copy()
    
    while vertices_a_visitar:
        vertice_atual = min(vertices_a_visitar, key=lambda vertice: distancias[vertice])
        for vizinho, peso in grafo.vertices[vertice_atual].items():
            rota_alternativa = distancias[vertice_atual] + peso
            if rota_alternativa < distancias[vizinho]:
                distancias[vizinho] = rota_alternativa
                caminho[vizinho] = vertice_atual
        vertices_a_visitar.pop(vertice_atual)
    
    return distancias, caminho

def caminho_mais_curto(caminho, inicio, fim):
    percurso = []
    passo = fim
    while passo is not None:
        percurso.insert(0, passo)
        passo = caminho[passo]
    return percurso if percurso[0] == inicio else []