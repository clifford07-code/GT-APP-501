import networkx as nx
import matplotlib.pyplot as plt
G1 = nx.Graph()
edges1 = [
    ('A','B','e1'), ('B','C','e2'), ('C','D','e3'), ('D','A','e4'),
    ('D','H','e5'), ('H','G','e6'), ('H','E','e7'),
    ('G','F','e8'), ('C','G','e9'), ('E','F','e10'),
    ('A','E','e11'), ('B','F','e12')
]
for u,v,e in edges1:
    G1.add_edge(u,v,label=e)
pos1 = {
    'A': (2, 2), 'B': (2, 0), 'C': (0, 0), 'D': (0, 2),
    'E': (1.5, 1.5), 'F': (1.5, 0.5),
    'G': (0.5, 0.5), 'H': (0.5, 1.5)
}
G2 = nx.Graph()
edges2 = [
    ('A', 'F','e1'), ('A', 'B','e2'), ('B', 'C','e3'), ('C', 'D','e4'),
    ('D', 'E','e5'), ('E', 'F','e6'), ('F', 'G','e7'), ('A', 'E','e8'),
    ('E', 'G','e9'), ('A', 'G','e10'), ('B', 'D','e11'), ('G', 'C','e12'),
    ('F','B','e13'), ('F','D','e14'), ('F','C','e15')
]
for u,v,e in edges2:
    G2.add_edge(u,v,label=e)
curved_bridge = ('F','C')
pos2 = {
    'A': (1, 2), 'B': (3, 2), 'C': (4, 1),
    'D': (3, 0), 'E': (1, 0), 'F': (0, 1), 'G': (2, 1)
}
plt.figure(figsize=(14,6))
plt.subplot(1,2,1)
nx.draw(G1, pos1, with_labels=True, node_color='lightblue', node_size=1200)
edge_labels1 = {(u,v):d['label'] for u,v,d in G1.edges(data=True)}
nx.draw_networkx_edge_labels(G1, pos1, edge_labels=edge_labels1)
plt.title("Graph (a)")
plt.subplot(1,2,2)
nx.draw_networkx_nodes(G2, pos2, node_size=1200, node_color='lightgreen')
nx.draw_networkx_labels(G2, pos2)
standard_edges = [e for e in G2.edges() if set(e) != set(curved_bridge)]
nx.draw_networkx_edges(G2, pos2, edgelist=standard_edges, width=2)
nx.draw_networkx_edges(
    G2, pos2,
    edgelist=[curved_bridge],
    connectionstyle='arc3,rad=0.8',
    arrows=True,
    arrowsize=0,
    width=2
)
edge_labels2 = {(u,v):d['label'] for u,v,d in G2.edges(data=True)}
nx.draw_networkx_edge_labels(G2, pos2, edge_labels=edge_labels2)
plt.title("Graph (b)")
plt.axis('off')
plt.tight_layout()
plt.show()
print("Graph (a) Eulerian:", nx.is_eulerian(G1))
print("Graph (b) Eulerian:", nx.is_eulerian(G2))
if nx.is_eulerian(G2):
    circuit = list(nx.eulerian_circuit(G2))
    path = " -> ".join([u for u,v in circuit] + [circuit[-1][1]])
    print("Eulerian Circuit:", path)