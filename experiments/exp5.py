import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations
G = nx.Graph()
edges = [
    (0, 1, 3),
    (0, 3, 6),
    (0, 2, 1),
    (1, 2, 5),
    (1, 4, 3),
    (2, 3, 5),
    (2, 4, 6),
    (2, 5, 4),
    (3, 5, 2),
    (4, 5, 6)
]
G.add_weighted_edges_from(edges)
L = nx.Graph()
edge_nodes = [(u, v) for u, v, w in edges]
L.add_nodes_from(edge_nodes)
for (e1, e2) in combinations(edge_nodes, 2):
    if len(set(e1) & set(e2)) > 0:  
        L.add_edge(e1, e2)
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
pos_G = {
    0: (0, 2),
    1: (-2, 1),
    3: (2, 1),
    2: (0, 0),
    4: (-2, -1),
    5: (2, -1)
}

nx.draw(G, pos_G, with_labels=True, node_color='lightblue', node_size=1000)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos_G, edge_labels=edge_labels)
plt.title("Original Graph")
plt.subplot(1, 2, 2)
pos_L = nx.spring_layout(L)
nx.draw(L, pos_L, with_labels=True, node_color='lightgreen', node_size=1200, font_size=8)
plt.title("Line Graph (Manual Construction)")
plt.tight_layout()
plt.show()