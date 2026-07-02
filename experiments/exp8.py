import networkx as nx
import matplotlib.pyplot as plt
import random
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
    ('A', 'F', 'e1'), ('A', 'B', 'e2'), ('B', 'C', 'e3'),
    ('C', 'D', 'e4'), ('D', 'E', 'e5'), ('E', 'F', 'e6'),
    ('F', 'G', 'e7'), ('A', 'E', 'e8'), ('E', 'G', 'e9'),
    ('A', 'G', 'e10'), ('B', 'D', 'e11'), ('G', 'C', 'e12')
]

for u, v, e in edges2:
    G2.add_edge(u, v, label=e)
pos2 = {
    'A': (1, 2), 'B': (3, 2), 'C': (4, 1),
    'D': (3, 0), 'E': (1, 0), 'F': (0, 1), 'G': (2, 1)
}
edge_labels2 = {
    ('A', 'F'): 'e1', ('A', 'B'): 'e2', ('B', 'C'): 'e3', ('C', 'D'): 'e4',
    ('D', 'E'): 'e5', ('E', 'F'): 'e6', ('F', 'G'): 'e7', ('A', 'E'): 'e8',
    ('E', 'G'): 'e9', ('A', 'G'): 'e10', ('B', 'D'): 'e11', ('G', 'C'): 'e12'
}
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
nx.draw(G1, pos1, with_labels=True, node_color='lightblue', node_size=1200)
edge_labels1 = {(u,v):d['label'] for u,v,d in G1.edges(data=True)}
nx.draw_networkx_edge_labels(G1, pos1, edge_labels=edge_labels1)
plt.title("Graph (a)")
plt.subplot(1,2,2)
nx.draw_networkx_nodes(G2, pos2, node_size=1000, node_color='lightgreen')
nx.draw_networkx_edges(G2, pos2, width=2)
nx.draw_networkx_labels(G2, pos2, font_size=16)
nx.draw_networkx_edge_labels(G2, pos2, edge_labels=edge_labels2)
plt.title("Graph (b)")
plt.axis('off')
plt.tight_layout()
plt.show()
def print_path(graph, path):
    result = []
    for i in range(len(path)-1):
        u = path[i]
        v = path[i+1]
        
        if graph.has_edge(u, v):
            e = graph[u][v]['label']
        elif graph.has_edge(v, u):
            e = graph[v][u]['label']
        else:
            return "Invalid path"

        result.append(f"{u}  {e}")
    result.append(path[0])
    return "   ".join(result)
def generate_closed_walk(graph, start, steps=6):
    walk = [start]
    current = start
    for _ in range(steps):
        neighbors = list(graph.neighbors(current))
        next_node = random.choice(neighbors)
        walk.append(next_node)
        current = next_node
    if walk[-1] != start:
        if graph.has_edge(current, start):
            walk.append(start)
        else:
            for n in graph.neighbors(current):
                if graph.has_edge(n, start):
                    walk.append(n)
                    walk.append(start)
                    break
    return walk
print("\nGRAPH (a)")
cycles1 = nx.cycle_basis(G1)
if cycles1:
    cycle = cycles1[0]
    cycle.append(cycle[0])
    print("Closed Path =", print_path(G1, cycle))
    print("Closed Trail =", print_path(G1, cycle))
walk_a = generate_closed_walk(G1, 'A')
print("Closed Walk =", print_path(G1, walk_a))
print("\nGRAPH (b)")
cycles2 = nx.cycle_basis(G2)
if cycles2:
    cycle = cycles2[0]
    cycle.append(cycle[0])
    print("Closed Path =", print_path(G2, cycle))
    print("Closed Trail =", print_path(G2, cycle))
walk_b = generate_closed_walk(G2, 'A')
print("Closed Walk =", print_path(G2, walk_b))