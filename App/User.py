from Backend.Dijkistra import caminho_mais_curto, dijkstra
from Backend.Grafo import Grafo


def main():
    grafo = Grafo()
    grafo.adicionar_aresta('A', 'B', 1)
    grafo.adicionar_aresta('A', 'C', 4)
    grafo.adicionar_aresta('B', 'C', 2)
    grafo.adicionar_aresta('B', 'D', 5)
    grafo.adicionar_aresta('C', 'D', 1)
    
    print("Grafo:")
    print(grafo)
    
    inicio = 'A'
    fim = 'D'
    distancias, caminho = dijkstra(grafo, inicio)
    percurso = caminho_mais_curto(caminho, inicio, fim)
    
    print(f"Distância mais curta de {inicio} para {fim}: {distancias[fim]}")
    print(f"Caminho: {' -> '.join(percurso)}")

if __name__ == "__main__":
    main()
