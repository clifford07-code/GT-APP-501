import networkx as nx
import matplotlib.pyplot as plt
import math

def build_graphs():
    g1 = nx.Graph()
    edges1 = [('A','B','e1'), ('B','C','e2'), ('C','D','e3'), ('D','A','e4'), ('D','H','e5'), 
              ('H','G','e6'), ('H','E','e7'), ('G','F','e8'), ('C','G','e9'), ('E','F','e10'), 
              ('A','E','e11'), ('B','F','e12')]
    for u, v, e in edges1:
        g1.add_edge(u, v, label=e)
    g2 = nx.Graph()
    edges2 = [('A', 'F','e1'), ('A', 'B','e2'), ('B', 'C','e3'), ('C', 'D','e4'), ('D', 'E','e5'), 
              ('E', 'F','e6'), ('F', 'G','e7'), ('A', 'E','e8'), ('E', 'G','e9'), ('A', 'G','e10'), 
              ('B', 'D','e11'), ('G', 'C','e12'), ('F','B','e13'), ('F','D','e14'), ('F','C','e15')]
    for u, v, e in edges2:
        g2.add_edge(u, v, label=e)
    return g1, g2

G1, G2 = build_graphs()
pos1 = {'A': (2, 2), 'B': (2, 0), 'C': (0, 0), 'D': (0, 2), 'E': (1.5, 1.5), 'F': (1.5, 0.5), 'G': (0.5, 0.5), 'H': (0.5, 1.5)}
pos2 = {'A': (1, 2), 'B': (3, 2), 'C': (4, 1), 'D': (3, 0), 'E': (1, 0), 'F': (0, 1), 'G': (2, 1)}
curved_bridge = ('F', 'C')

def check_eulerian_manual(G):
    for node in G.nodes():
        if G.degree(node) % 2 != 0:
            return False
    start = list(G.nodes())[0]
    visited, stack = set(), [start]
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            for neighbor in G.neighbors(current):
                if neighbor not in visited:
                    stack.append(neighbor)
    return len(visited) == len(G.nodes())

is_g1_eulerian = check_eulerian_manual(G1)
is_g2_eulerian = check_eulerian_manual(G2)
print("Graph (a) Eulerian :", is_g1_eulerian)
print("Graph (b) Eulerian :", is_g2_eulerian)
if nx.is_eulerian(G2):
    euler_path = list(nx.eulerian_circuit(G2, source='A'))
    total_steps = len(euler_path)
    cols = 3
    rows = math.ceil(total_steps / cols)
    fig, axes = plt.subplots(rows, cols, figsize=(18, rows * 4))
    axes = axes.flatten() if total_steps > 1 else [axes]
    for idx in range(total_steps):
        ax = axes[idx]
        nx.draw_networkx_nodes(G2, pos2, node_color='lightgreen', node_size=1000, ax=ax)
        nx.draw_networkx_labels(G2, pos2, font_size=10, font_weight='bold', ax=ax)
        normal_edges = [e for e in G2.edges() if set(e) != set(curved_bridge)]
        nx.draw_networkx_edges(G2, pos2, edgelist=normal_edges, edge_color='lightgray', width=1, ax=ax)
        nx.draw_networkx_edges(G2, pos2, edgelist=[curved_bridge], edge_color='lightgray', connectionstyle='arc3,rad=0.8', width=1, ax=ax)
        used_edges = euler_path[:idx + 1]
        used_normal = [e for e in used_edges if set(e) != set(curved_bridge)]
        used_curved = [e for e in used_edges if set(e) == set(curved_bridge)]
        nx.draw_networkx_edges(G2, pos2, edgelist=used_normal, edge_color='red', width=3, ax=ax)
        if used_curved:
            nx.draw_networkx_edges(G2, pos2, edgelist=used_curved, edge_color='red', connectionstyle='arc3,rad=0.8', width=3, ax=ax)
        edge_labels = {(u, v): d['label'] for u, v, d in G2.edges(data=True)}
        nx.draw_networkx_edge_labels(G2, pos2, edge_labels=edge_labels, font_size=7, ax=ax)
        ax.axis('off')
    for j in range(total_steps, len(axes)):
        fig.delaxes(axes[j])
    plt.tight_layout(rect=[0, 0, 1, 0.97])
    plt.suptitle("Eulerian Circuit Traversal", fontsize=20)
    plt.show()