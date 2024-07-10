import os
import plotly.graph_objs as go
import networkx as nx

def generate_plotly_diagram(base_path, output_path):
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
    edge_x = []
    edge_y = []

    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=0.5, color='#888'),
        hoverinfo='none',
        mode='lines')

    node_x = []
    node_y = []

    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        text=[G.nodes[node]['label'] for node in G.nodes()],
        hoverinfo='text',
        marker=dict(
            showscale=True,
            colorscale='YlGnBu',
            reversescale=True,
            color=[],
            size=10,
            colorbar=dict(
                thickness=15,
                title='Node Connections',
                xanchor='left',
                titleside='right'
            ),
            line_width=2))

    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        title='<br>Project Architecture',
                        titlefont_size=16,
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=20,l=5,r=5,t=40),
                        annotations=[ dict(
                            text="",
                            showarrow=False,
                            xref="paper", yref="paper") ],
                        xaxis=dict(showgrid=False, zeroline=False),
                        yaxis=dict(showgrid=False, zeroline=False))
                    )
    fig.write_image(output_path)

if __name__ == "__main__":
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    output_path = os.path.join(base_path, 'docs', 'architecture', 'plotly_architecture.png')
    generate_plotly_diagram(base_path, output_path)
