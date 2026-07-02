import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
edges = [
    (0, 1, 3), (0, 3, 6), (0, 2, 1),
    (1, 2, 5), (1, 4, 3),
    (2, 3, 5), (2, 4, 6), (2, 5, 4),
    (3, 5, 2),
    (4, 5, 6)
]
G.add_weighted_edges_from(edges)
pos = {
    0: (0, 2),
    1: (-1, 1),
    2: (0, 0),
    3: (1, 1),
    4: (-1, -1),
    5: (1, -1)
}
source = 0
lengths, paths = nx.single_source_dijkstra(G, source)
print("Shortest Paths from Source:", source)
for node in sorted(paths):
    print(f"{source} → {node}: Path = {paths[node]}, Cost = {lengths[node]}")
plt.figure(figsize=(6,6))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
path_edges = []
for target in paths:
    path = paths[target]
    for i in range(len(path)-1):
        path_edges.append((path[i], path[i+1]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
plt.title("Shortest Path (Dijkstra)")
plt.show()