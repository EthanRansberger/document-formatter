import os
import matplotlib.pyplot as plt
import networkx as nx

def generate_matplotlib_diagram(base_path, output_path):
    G = nx.Graph()

    for root, dirs, files in os.walk(base_path):
        for name in dirs:
            dir_path = os.path.join(root, name)
            G.add_node(dir_path, label=name, shape='folder')
            if root != base_path:
                G.add_edge(root, dir_path)

        for name in files:
            file_path = os.path.join(root, name)
            G.add_node(file_path, label=name, shape='note')
            if root != base_path:
                G.add_edge(root, file_path)
    
    pos = nx.spring_layout(G)
    plt.figure()
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightgreen', font_size=10)
    plt.savefig(output_path)

if __name__ == "__main__":
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    output_path = os.path.join(base_path, 'docs', 'architecture', 'matplotlib_architecture.png')
    generate_matplotlib_diagram(base_path, output_path)
