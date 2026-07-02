import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
edges = [
    (1, 2, 15), (1, 3, 14), (1, 5, 3),
    (3, 5, 9), (3, 6, 8),
    (5, 6, 15),
    (3, 4, 6),
    (4, 2, 2), (4, 7, 3), (4, 8, 9),
    (2, 8, 17),
    (7, 8, 2),
    (6, 7, 8), (6, 4, 9)
]
G.add_weighted_edges_from(edges)
pos = {
    1: (1, 3),
    2: (6, 3),
    3: (3, 1.5),
    4: (6, 1.5),
    5: (0, 0),
    6: (3, 0),
    7: (6, 0),
    8: (8, 1.5)
}
mst = nx.minimum_spanning_tree(G, algorithm='kruskal')
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
nx.draw(G, pos, with_labels=True, node_color='yellow',
        node_size=800, edgecolors="black")
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Original Graph")
plt.subplot(1, 2, 2)
nx.draw(mst, pos, with_labels=True, node_color='lightgreen',
        node_size=800, edgecolors="black")
labels = nx.get_edge_attributes(mst, 'weight')
nx.draw_networkx_edge_labels(mst, pos, edge_labels=labels)
plt.title("Minimum Spanning Tree (Kruskal)")
plt.tight_layout()
plt.show()
cost = sum(d['weight'] for u, v, d in mst.edges(data=True))
print("Total cost of MST:", cost)