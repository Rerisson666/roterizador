import heapq

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

def dijkstra(grafo, inicio):
    distancias = {vertice: float('infinity') for vertice in grafo.vertices}
    distancias[inicio] = 0
    caminho = {vertice: None for vertice in grafo.vertices}
    
    fila_prioridade = [(0, inicio)]
    while fila_prioridade:
        distancia_atual, vertice_atual = heapq.heappop(fila_prioridade)
        
        if distancia_atual > distancias[vertice_atual]:
            continue
        
        for vizinho, peso in grafo.vertices[vertice_atual]:
            distancia = distancia_atual + peso
            
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                caminho[vizinho] = vertice_atual
                heapq.heappush(fila_prioridade, (distancia, vizinho))
    
    return distancias, caminho

def caminho_mais_curto(caminho, inicio, fim):
    percurso = []
    atual = fim
    while atual is not None:
        percurso.append(atual)
        atual = caminho[atual]
    percurso.reverse()
    return percurso
