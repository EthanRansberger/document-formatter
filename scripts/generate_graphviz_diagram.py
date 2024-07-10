import os
from graphviz import Digraph

def generate_graphviz_diagram(base_path, output_path):
    dot = Digraph(comment='Project Architecture')

    for root, dirs, files in os.walk(base_path):
        for name in dirs:
            dir_path = os.path.join(root, name)
            dot.node(dir_path, label=name, shape='folder')
            if root != base_path:
                dot.edge(root, dir_path)

        for name in files:
            file_path = os.path.join(root, name)
            dot.node(file_path, label=name, shape='note')
            if root != base_path:
                dot.edge(root, file_path)
    
    dot.render(output_path, format='png')

if __name__ == "__main__":
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    output_path = os.path.join(base_path, 'docs', 'architecture', 'graphviz_architecture')
    generate_graphviz_diagram(base_path, output_path)
