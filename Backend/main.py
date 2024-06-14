import tkinter as tk
from tkinter import messagebox
from Backend import Grafo, dijkstra, caminho_mais_curto

class App:
    def __init__(self, root):
        self.grafo = Grafo()
        self.root = root
        self.root.title("Algoritmo de Roteamento - Dijkstra")
        
        self.frame = tk.Frame(root)
        self.frame.pack(pady=20)
        
        self.vertice_label = tk.Label(self.frame, text="Vértice:")
        self.vertice_label.grid(row=0, column=0)
        self.vertice_entry = tk.Entry(self.frame)
        self.vertice_entry.grid(row=0, column=1)
        self.vertice_button = tk.Button(self.frame, text="Adicionar Vértice", command=self.adicionar_vertice)
        self.vertice_button.grid(row=0, column=2)
        
        self.origem_label = tk.Label(self.frame, text="Origem:")
        self.origem_label.grid(row=1, column=0)
        self.origem_entry = tk.Entry(self.frame)
        self.origem_entry.grid(row=1, column=1)
        
        self.destino_label = tk.Label(self.frame, text="Destino:")
        self.destino_label.grid(row=2, column=0)
        self.destino_entry = tk.Entry(self.frame)
        self.destino_entry.grid(row=2, column=1)
        
        self.peso_label = tk.Label(self.frame, text="Peso:")
        self.peso_label.grid(row=3, column=0)
        self.peso_entry = tk.Entry(self.frame)
        self.peso_entry.grid(row=3, column=1)
        
        self.aresta_button = tk.Button(self.frame, text="Adicionar Aresta", command=self.adicionar_aresta)
        self.aresta_button.grid(row=4, column=1)
        
        self.inicio_label = tk.Label(self.frame, text="Início:")
        self.inicio_label.grid(row=5, column=0)
        self.inicio_entry = tk.Entry(self.frame)
        self.inicio_entry.grid(row=5, column=1)
        
        self.fim_label = tk.Label(self.frame, text="Fim:")
        self.fim_label.grid(row=6, column=0)
        self.fim_entry = tk.Entry(self.frame)
        self.fim_entry.grid(row=6, column=1)
        
        self.calcular_button = tk.Button(self.frame, text="Calcular Rota", command=self.calcular_rota)
        self.calcular_button.grid(row=7, column=1)
        
        self.resultado_label = tk.Label(self.frame, text="")
        self.resultado_label.grid(row=8, column=0, columnspan=3)
    
    def adicionar_vertice(self):
        vertice = self.vertice_entry.get()
        if vertice:
            self.grafo.adicionar_vertice(vertice)
            messagebox.showinfo("Sucesso", f"Vértice {vertice} adicionado.")
        else:
            messagebox.showerror("Erro", "Por favor, insira um vértice válido.")
    
    def adicionar_aresta(self):
        origem = self.origem_entry.get()
        destino = self.destino_entry.get()
        peso = self.peso_entry.get()
        
        if origem and destino and peso:
            try:
                peso = float(peso)
                self.grafo.adicionar_aresta(origem, destino, peso)
                messagebox.showinfo("Sucesso", f"Aresta de {origem} para {destino} com peso {peso} adicionada.")
            except ValueError:
                messagebox.showerror("Erro", "Por favor, insira um peso válido.")
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos para adicionar uma aresta.")
    
    def calcular_rota(self):
        inicio = self.inicio_entry.get()
        fim = self.fim_entry.get()
        
        if inicio and fim:
            if inicio in self.grafo.vertices and fim in self.grafo.vertices:
                distancias, caminho = dijkstra(self.grafo, inicio)
                percurso = caminho_mais_curto(caminho, inicio, fim)
                distancia = distancias[fim]
                self.resultado_label.config(text=f"Distância: {distancia}\nCaminho: {' -> '.join(percurso)}")
            else:
                messagebox.showerror("Erro", "Por favor, insira vértices válidos que estão no grafo.")
        else:
            messagebox.showerror("Erro", "Por favor, preencha os campos de início e fim.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
