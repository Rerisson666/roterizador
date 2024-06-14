from flask import Flask, render_template, request, redirect, url_for, flash
from algoritmo import Grafo, dijkstra, caminho_mais_curto

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Substitua 'your_secret_key' por uma chave secreta adequada

# Inicialize o grafo globalmente
grafo = Grafo()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adicionar_vertice', methods=['POST'])
def adicionar_vertice():
    vertice = request.form['vertice']
    if vertice:
        grafo.adicionar_vertice(vertice)
        flash(f"Vértice {vertice} adicionado.", "success")
    else:
        flash("Por favor, insira um vértice válido.", "error")
    return redirect(url_for('index'))

@app.route('/adicionar_aresta', methods=['POST'])
def adicionar_aresta():
    origem = request.form['origem']
    destino = request.form['destino']
    peso = request.form['peso']
    
    if origem and destino and peso:
        try:
            peso = float(peso)
            grafo.adicionar_aresta(origem, destino, peso)
            flash(f"Aresta de {origem} para {destino} com peso {peso} adicionada.", "success")
        except ValueError:
            flash("Por favor, insira um peso válido.", "error")
    else:
        flash("Por favor, preencha todos os campos para adicionar uma aresta.", "error")
    return redirect(url_for('index'))

@app.route('/calcular_rota', methods=['POST'])
def calcular_rota():
    inicio = request.form['inicio']
    fim = request.form['fim']
    
    if inicio and fim:
        if inicio in grafo.vertices and fim in grafo.vertices:
            distancias, caminho = dijkstra(grafo, inicio)
            percurso = caminho_mais_curto(caminho, inicio, fim)
            distancia = distancias[fim]
            return render_template('index.html', distancia=distancia, percurso=percurso)
        else:
            flash("Por favor, insira vértices válidos que estão no grafo.", "error")
    else:
        flash("Por favor, preencha os campos de início e fim.", "error")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)