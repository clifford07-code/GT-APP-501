import networkx as nx
import matplotlib.pyplot as plt
import math
G = nx.Graph()
edges = [
    (0,1,3),(0,3,6),(0,2,1),
    (1,2,5),(1,4,3),
    (2,3,5),(2,4,6),(2,5,4),
    (3,5,2),
    (4,5,6)
]
G.add_weighted_edges_from(edges)
source = 0
pos = {
    0: (0, 2),
    1: (-1, 1),
    2: (0, 0),
    3: (1, 1),
    4: (-1, -1),
    5: (1, -1)
}
nodes = list(G.nodes())
dist = {node: math.inf for node in nodes}
prev = {node: None for node in nodes}
visited = []
dist[source] = 0
steps = []
while len(visited) < len(nodes):
    current = None
    min_dist = math.inf
    for node in nodes:
        if node not in visited and dist[node] < min_dist:
            min_dist = dist[node]
            current = node
    if current is None:
        break
    visited.append(current)
    for neighbor in G.neighbors(current):
        weight = G[current][neighbor]['weight']
        if dist[current] + weight < dist[neighbor]:
            dist[neighbor] = dist[current] + weight
            prev[neighbor] = current
    current_paths = {}
    for node in nodes:
        path = []
        temp = node
        while temp is not None:
            path.insert(0, temp)
            temp = prev[temp]
        if path and path[0] == source:
            current_paths[node] = path
    steps.append((current_paths.copy(), visited.copy()))
fig, axes = plt.subplots(2, 3, figsize=(12, 8))
axes = axes.flatten()
for step, (paths, vis) in enumerate(steps):
    ax = axes[step]
    nx.draw(G, pos, ax=ax, with_labels=True,
            node_size=1200, node_color='lightblue')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)
    highlight_edges = []
    for path in paths.values():
        for i in range(len(path)-1):
            highlight_edges.append((path[i], path[i+1]))
    nx.draw_networkx_edges(
        G, pos, edgelist=highlight_edges,
        edge_color='red', width=2, ax=ax
    )
    ax.set_title(f"Step {step+1}\nVisited: {vis}")
    ax.axis('off')
for i in range(len(steps), len(axes)):
    axes[i].axis('off')
plt.suptitle("Dijkstra Step-by-Step (Your Graph)", fontsize=16)
plt.tight_layout()
plt.show()
print("Shortest Paths from Source:", source)
for node in nodes:
    path = []
    temp = node
    while temp is not None:
        path.insert(0, temp)
        temp = prev[temp]
    print(f"{source} → {node}: Path = {path}, Cost = {dist[node]}")

