import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
nodes = list(range(1, 13))
G.add_nodes_from(nodes)
edges = [
    (1,2), (2,3), (3,4),
    (5,6), (6,7), (7,8),
    (9,10), (10,11), (11,12),
    (1,5), (5,9),
    (2,6), (6,10),
    (3,7), (7,11),
    (4,8), (8,12)
]
G.add_edges_from(edges)
pos = {
    1:(0,2), 2:(2,2), 3:(4,2), 4:(6,2),
    5:(0,1), 6:(2,1), 7:(4,1), 8:(6,1),
    9:(0,0), 10:(2,0), 11:(4,0), 12:(6,0)
}
plt.figure(figsize=(10,6))
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=1400,
    node_color='white',
    edgecolors='black',
    linewidths=2,
    width=2,
    font_size=12,
    font_weight='bold'
)
plt.title("Original Graph")
plt.axis('off')
plt.show()
def find_hamiltonian_circuit(graph):
    n = len(graph.nodes)
    def backtrack(path):
        if len(path) == n:
            if graph.has_edge(path[-1], path[0]):
                path.append(path[0])
                return path
            return None
        current = path[-1]
        for neighbor in graph.neighbors(current):
            if neighbor not in path:
                path.append(neighbor)
                result = backtrack(path)
                if result:
                    return result
                path.pop()
        return None
    return backtrack([1])
hamiltonian_circuit = find_hamiltonian_circuit(G)
print("Hamiltonian Circuit Found:")
print(hamiltonian_circuit)
fig, axes = plt.subplots(4,4, figsize=(18,14))
axes = axes.flatten()
visited = []
for i in range(len(hamiltonian_circuit)):
    visited.append(hamiltonian_circuit[i])
    ax = axes[i]
    nx.draw(
        G,
        pos,
        ax=ax,
        with_labels=True,
        node_size=1000,
        node_color='white',
        edgecolors='black',
        linewidths=2,
        width=2,
        font_weight='bold'
    )
    path_edges = []
    for j in range(len(visited)-1):
        path_edges.append((visited[j], visited[j+1]))
    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=path_edges,
        edge_color='red',
        width=4,
        ax=ax
    )
    ax.set_title(f"Step {i+1}\nVisited: {visited}")
    ax.axis('off')
for k in range(len(hamiltonian_circuit), len(axes)):
    fig.delaxes(axes[k])
plt.suptitle("Hamiltonian Circuit Step-by-Step", fontsize=22)
plt.tight_layout()
plt.show()