## Passos para criar o aplicativo:

Instalação do Tkinter: Normalmente, o Tkinter já vem instalado com o Python, mas você pode garantir isso instalando-o através do gerenciador de pacotes do seu sistema, caso não esteja disponível.

Criação da Interface do Usuário: Usaremos o Tkinter para criar uma janela onde o usuário pode inserir vértices, arestas e seus pesos, e selecionar os pontos de início e fim.

Integração do Algoritmo com a Interface: Conectar os inputs da interface gráfica com a lógica do algoritmo.

Código do Aplicativo
Vamos começar com uma versão básica da interface e, em seguida, integrar o algoritmo de Dijkstra.

## Estrutura do Projeto
# main.py: Código principal do aplicativo.
# algoritmo.py: Implementação do grafo e do algoritmo de Dijkstra.

## Explicação

# Interface do Usuário:

Labels e Entries para inserir vértices, arestas, pesos, ponto inicial e final.
Botões para adicionar vértices, adicionar arestas e calcular a rota.
Um label para mostrar o resultado do cálculo da rota.
Funcionalidade:

Os métodos adicionar_vertice, adicionar_aresta e calcular_rota conectam a interface com a lógica do algoritmo.
adicionar_vertice e adicionar_aresta atualizam o grafo conforme os inputs do usuário.
calcular_rota usa o algoritmo de Dijkstra para calcular a rota mais curta e exibe o resultado na interface.
Uso do Tkinter:

Tkinter é usado para criar e organizar widgets (botões, labels, entries) e manipular eventos (cliques de botão).
Essa estrutura básica pode ser expandida conforme necessário, adicionando mais funcionalidades ou refinando a interface para uma melhor usabilidade.